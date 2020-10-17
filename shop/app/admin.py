from django.contrib import admin
from .models import Category, Product, Image

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'alt', 'product', 'primary']
    list_filter = ['url', 'name', 'alt', 'product']
    list_editable = ['name', 'alt', 'product', 'primary']
