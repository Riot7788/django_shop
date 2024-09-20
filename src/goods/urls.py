from django.urls import path


from .views import (
    catalog,
    product,
)


urlpatterns = [
    path('', catalog, {'category_slug': 'all'}, name='catalog_all'),
    path('<slug:category_slug>/', catalog, name='index'),
    path('product/<slug:product_slug>/', product, name="product"),
]
