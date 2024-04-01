from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer
from .models import Product
from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

description_analyzer = analyzer(
    "description_analyzer",
    tokenizer="standard",
    filter=["lowercase", "stop", "ngram"],
)


@registry.register_document
class ProductDocument(Document):
    name = fields.TextField()
    description = fields.TextField(analyzer=description_analyzer)
    price = fields.FloatField()

    class Index:
        name = "product_index"

    class Django:
        model = Product
