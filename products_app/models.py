from django.db import models
from users_app.models import Users


class ProductCategory(models.Model):
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} --> {self.category}"
    

class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(bask.quantity for bask in self)

    
    def total_price(self):
        basket_price = 0
        for bask in self:
            basket_price+=bask.get_price()
        return basket_price


class Basket(models.Model):
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"{self.user.username} uchun savat, mahsulot: {self.product.name}"
    
    def get_price(self):
        return self.product.price*self.quantity
    
    
