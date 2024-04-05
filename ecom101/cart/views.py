from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.http import JsonResponse
from app.models import Product


def cart_add(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        cart = Cart(request)
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        # response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response


# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities})


def cart_delete(request):
    return render(request, "cart_delete.html", {})


def cart_update(request):
    return render(request, "cart_update.html", {})

