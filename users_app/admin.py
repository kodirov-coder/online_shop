from django.contrib import admin

from .models import Users
from products_app.admin import BasketAdmin


# admin.site.register(Users)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username", "last_name")
    inlines = (BasketAdmin, )