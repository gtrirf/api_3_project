from django.urls import path
from .views import CreateProductListView, ListProductView

urlpatterns = [
    path('create-or-list/', CreateProductListView.as_view(), name='create'),
    path('list/<int:pk>/', ListProductView.as_view(), name='list'),
]