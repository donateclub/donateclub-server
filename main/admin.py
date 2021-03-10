from django.contrib import admin
from .models import *

class ProductInline(admin.TabularInline):
    model = Product
    fields = ['title', 'ngo', 'issue']
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'ngo', 'issue']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['name']

@admin.register(Ngo)
class NgoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']