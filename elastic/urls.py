from django.urls import path
from . import views
from .views import ProductSearchView

urlpatterns = [
    path("", ProductSearchView.as_view(), name="search_view"),
]
