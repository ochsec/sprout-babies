import json
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Image
from cart.forms import CartAddProductForm

def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product_search = [{'name': p.name, 'url': p.get_absolute_url()} for p in products]
    return render(request,
        'app/home.html',
        {'categories': categories,
        'product_search': json.dumps(product_search)})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product_search = [{'name': p.name, 'url': p.get_absolute_url()} for p in products]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    images = Image.objects.filter(primary=True)
    for index, p in enumerate(products):
        p_images = images.filter(product=p.id)
        for i in p_images:
            if i.primary:
                products[index].image_url = str(i.url)
                break

    return render(request,
        'app/product/list.html',
        {'category': category,
        'product_search': json.dumps(product_search),
        'categories': categories,
        'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
        id=id,
        slug=slug,
        available=True)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product_search = [{'name': p.name, 'url': p.get_absolute_url()} for p in products]
    images = Image.objects.filter(product=product.id)

    # for i in images:
    #     if i.primary:
    #         product.image_url = str(i.url)

    return render(request,
        'app/product/detail.html',
        {'product': product,
        'categories': categories,
        'images': images,
        'product_search': json.dumps(product_search),
        'cart_product_form': cart_product_form})

