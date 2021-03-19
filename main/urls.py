from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from .serializers import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_collection'),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('ngos/', NgoList.as_view(), name='ngo_collection'),
    path('issues/', IssuesList.as_view(), name='issues_collection'),
    path('posts/', BlogsList.as_view(), name='blog_post_collection'),
    path('doantions/', DonationsList.as_view(), name='donation_collection'),
    path('badges/', BadgesList.as_view(), name='badge_collection'),
    path('services/', ServicesList.as_view, name='service_collection'),
    path('users/', ClubUsersList.as_view(), name='user_collection'),
]


urlpatterns = format_suffix_patterns(urlpatterns)