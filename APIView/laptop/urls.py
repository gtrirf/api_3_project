from django.urls import path
from .views import ListCategory, ListLaptop, DetailLaptop

urlpatterns = [
    path('category/', ListCategory.as_view(), name='category'),
    path('laptop/', ListLaptop.as_view(), name='laptop'),
    path('laptop/<int:pk>/', DetailLaptop.as_view(), name='laptop_detail'),
]
