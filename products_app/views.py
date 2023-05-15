from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Product, ProductCategory, Basket


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Hush kelibsiz"
        return context

class ProductsListView(ListView):
    model = Product
    template_name = "products.html"
    paginate_by = 3
   
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        # return queryset.filter(category_id=category_id) if category_id else queryset
        if category_id:
            return queryset.filter(category_id=category_id)
        else:
            return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["title"] = "Mahsulotlar"
        context["categories"] = ProductCategory.objects.all()
        return context

# def products(request, category_id=None, page=1):
#     if category_id:
#         product = Product.objects.filter(category_id=category_id)
#     else:
#         product = Product.objects.all()
#     category = ProductCategory.objects.all()

#     per_page = 3
#     paginate = Paginator(product, per_page)
#     paginated_product = paginate.get_page(page)

#     context ={
#         "products": paginated_product,
#         "categories": category,
#         }

#     return render(request, "products.html", context)

@login_required
def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity+=1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def remove_from_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])