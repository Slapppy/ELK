from django.core.management.base import BaseCommand
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from django.apps import apps
from elasticsearch import Elasticsearch


class Command(BaseCommand):
    help = "Indexes all products into Elasticsearch"

    def handle(self, *args, **options):
        Product = apps.get_model("elastic", "Product")

        es = Elasticsearch(hosts=["localhost:9200"])

        product_index = Index("product_index")

        description_analyzer = analyzer(
            "description_analyzer",
            tokenizer="standard",
            filter=["lowercase", "stop", "snowball"],
        )

        class ProductDocument(Document):
            name = fields.TextField()
            description = fields.TextField(analyzer=description_analyzer)
            price = fields.FloatField()

            class Index:
                name = "product_index"

            class Django:
                model = Product

        ProductDocument.init(using=es)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully initialized Elasticsearch index for products"
            )
        )
