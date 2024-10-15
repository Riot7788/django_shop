from django.shortcuts import render, redirect


from goods.models import Products
from carts.models import Cart


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            action = request.GET.get('action')

            if action == "increment":
                # Увеличиваем количество товара на 1
                cart.quantity += 1
                cart.save()
            elif action == "decrement":
                # Уменьшаем количество товара на 1, если количество больше 1
                if cart.quantity > 1:
                    cart.quantity -= 1
                    cart.save()
                else:
                    # Если количество равно 1, удаляем товар из корзины
                    cart.delete()

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])
