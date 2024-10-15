from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Products


def home_view(request):

    sale_products = Products.objects.filter(discount__gt=0)

    context = {
        'sale_products': sale_products,
    }
    return render(
        request=request,
        template_name="home.html",
        context=context
    )


def about_us(request):
    return render(
        request=request,
        template_name="about.html"
    )


def contact_info(request):
    return render(
        request=request,
        template_name="contact_info.html"
    )


def comment_user(request):
    return render(
        request=request,
        template_name="comment_user.html"
    )

