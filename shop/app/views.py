from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

def home(request):
    categories = Category.objects.all()
    return render(request,
        'app/home.html',
        {'categories': categories})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
        'app/product/list.html',
        {'category': category,
        'categories': categories,
        'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
        'app/product/detail.html',
        {'product': product,
        'cart_product_form': cart_product_form})

