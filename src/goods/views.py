from django.shortcuts import render

from .models import Categories
from .models import Products


def catalog(request):

    categories = Categories.objects.all()
    goods = Products.objects.all()

    context = {
        'categories': categories,
        "goods": goods,
    }

    return render(
        request=request,
        template_name="goods/catalog.html",
        context=context
    )


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(
        request=request,
        template_name="goods/product.html",
        context=context
    )
