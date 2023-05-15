from django.urls import path

from .views import ProductsListView, add_to_basket, remove_from_basket

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-page"),
    path("category/<int:category_id>", ProductsListView.as_view(), name="category"),
    path("page/<int:page>", ProductsListView.as_view(), name="paginator"),
    path("add/<int:product_id>", add_to_basket, name="add_to_basket"),
    path("remove/<int:basket_id>", remove_from_basket, name="remove_from_basket"),
]