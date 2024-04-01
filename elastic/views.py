# benchmarks/views.py
import time
from django.shortcuts import render
from django.views import View

from ELK.settings import ELASTICSEARCH_DSL
from .models import Product
from elasticsearch import Elasticsearch


from django.shortcuts import render
from django.views import View
from elasticsearch import Elasticsearch
from elastic.document import ProductDocument


class ProductSearchView(View):
    def get(self, request):
        query = request.GET.get("query", "")

        es = Elasticsearch(hosts=["localhost:9200"])

        index_name = "product_index"

        search = (
            ProductDocument.search()
            .index(index_name)
            .query("multi_match", query=query, fields=["name^3", "description"])
            .extra(size=3)
        )

        response = search.execute()

        products = [hit.to_dict() for hit in response]
        print(products)
        return render(
            request,
            "elastic/product_search.html",
            {"products": products, "query": query},
        )
