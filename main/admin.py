from django.contrib import admin
from .models import *

class ProductInline(admin.TabularInline):
    model = Product
    fields = ['title', 'ngo', 'category']
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'ngo', 'category']

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['name']

@admin.register(Ngo)
class NgoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']