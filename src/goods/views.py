from django.shortcuts import render

from .models import Categories


def catalog(request):

    categories = Categories.objects.all()

    context = {
        'categories': categories
    }

    return render(
        request=request,
        template_name="goods/catalog.html",
        context=context
    )


def product(request):
    return render(
        request=request,
        template_name="goods/product.html"
    )
