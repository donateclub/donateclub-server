from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from .serializers import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_collection'),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('ngos/', NgoList.as_view(), name='ngo_collection'),
    path('ngos/<int:pk>/', NgoDetails.as_view(),),
    path('issues/', IssuesList.as_view(), name='issues_collection'),
    path('issues/<int:pk>/', IssueDetails.as_view(),),
    path('posts/', BlogsList.as_view(), name='blog_post_collection'),
    path('doantions/', DonationsList.as_view(), name='donation_collection'),
    path('badges/', BadgesList.as_view(), name='badge_collection'),
    path('services/', ServicesList.as_view, name='service_collection'),
    path('users/', ClubUsersList.as_view(), name='user_collection'),
    path('users/<int:pk>/', ClubUserDetail.as_view(), name='user_details'),
    path('contactUs/', ConatctUsList.as_view(), name='contact_put'),
    path('blog/<int:pk>/', BlogDetails.as_view(), name='blog_details'),
    path('blogs/', BlogsList.as_view(), name='blog_collection'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]