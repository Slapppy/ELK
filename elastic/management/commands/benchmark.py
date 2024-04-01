import time
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from elastic.models import Product
from elastic.document import ProductDocument


from django.core.management.base import BaseCommand
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from django.apps import apps
from elasticsearch import Elasticsearch
import time


class Command(BaseCommand):
    help = "Benchmark for Django ORM and Elasticsearch queries"

    def handle(self, *args, **options):
        num_records = 10000

        start_time = time.time()
        orm_results = list(
            Product.objects.filter(
                description="MxUTngax6XagmPttLH9r4U4CoaUmhrzRaX3uXwjhl4AoWENkZM"
            )
        )
        orm_time = time.time() - start_time
        print(orm_results)
        es = Elasticsearch(hosts=["localhost:9200"])
        index_name = "product_index"

        search = (
            ProductDocument.search()
            .index(index_name)
            .query(
                "match",
                description="MxUTngax6XagmPttLH9r4U4CoaUmhrzRaX3uXwjhl4AoWENkZM",
            )
        )

        start_time = time.time()
        es_results = [hit.to_dict() for hit in search.execute()]
        es_time = time.time() - start_time
        print(es_results)
        print(f"Django ORM Query Time: {str(orm_time)[:6]}")
        print(f"Elasticsearch Query Time: {str(es_time)[:6]}")


if __name__ == "__main__":
    Command().handle()
