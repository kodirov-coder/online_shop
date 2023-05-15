from django.contrib import admin
from .models import ProductCategory, Product, Basket


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "category")
    search_fields = ("name", )
    fields = ("name", "description", "image", ("price", "quantity"), "category")
    readonly_fields = ("description",)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0
