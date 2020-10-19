import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app.models import Category, Product, Image
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)

    products = Product.objects.filter(available=True)
    product_search = [{'name': p.name, 'url': p.get_absolute_url()} for p in products]
    categories = Category.objects.all()
    images = Image.objects.filter(primary=True)
    for item in cart:
        p_images = images.filter(product=item['product'].id)
        for i in p_images:
            if i.primary:
                item['image_url'] = str(i.url)
                break

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'categories': categories, 'product_search': json.dumps(product_search)})
