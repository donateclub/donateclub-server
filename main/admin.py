from django.contrib import admin
from .models import *

class ProductInline(admin.TabularInline):
    model = Product
    fields =  ['title', 'description', 'deadline', 'required', 'donated', 'issue', 'ngo', 'image']
    show_change_link = True

class NgoInline(admin.TabularInline):
    model = Ngo
    fields =  ['title', 'rating', 'year_established', 'description', 'country', 'state', 'city', 'pincode', 'issue', 'phone_number', 'email']
    show_change_link = True

class BlogPostInline(admin.TabularInline):
    model = BlogPost
    fields =  ['title', 'date_published', 'date_edited', 'body', 'ngo','issue']
    show_change_link = True

class BadgeInline(admin.TabularInline):
    model = UserBadge
    fields =  ['badge']
    show_change_link = True

class UserInline(admin.TabularInline):
    model = UserBadge
    fields =  ['user']
    show_change_link = True

class DonationInline(admin.TabularInline):
    model = Donation
    fields =  ['date', 'amount', 'user', 'product']
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'deadline', 'required', 'donated', 'issue', 'ngo', 'image']

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    inlines = [ProductInline, NgoInline, BlogPostInline, ]
    list_display = ['name', 'description']

@admin.register(Ngo)
class NgoAdmin(admin.ModelAdmin):
    inlines = [ProductInline, BlogPostInline]
    list_display = ['title', 'rating', 'year_established', 'description', 'country', 'state', 'city', 'pincode', 'issue', 'phone_number', 'email']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_published', 'date_edited', 'body', 'ngo','issue']


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'user', 'product']

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    inlines = [UserInline]
    list_display = ['title', 'description','threshold']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date', 'paid', 'salary', 'image', 'ngo', 'issue']


@admin.register(ClubUser)
class ClubUserAdmin(admin.ModelAdmin):
    inlines = [BadgeInline, DonationInline]
    list_display = ['username', 'image', 'email', 'phone_number', 'country', 'state', 'city']