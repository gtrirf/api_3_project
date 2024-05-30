from django.urls import path
from .views import get_user, put_user, create_user, delete_user, UserViewSet

urlpatterns = [
    path('list/', UserViewSet.as_view({'get': 'list'}), name='list'),
    path('create', create_user, name='create'),
    path('get', get_user, name='get'),
    path('update/<int:pk>/', put_user, name='update'),
    path('delete/<int:pk>/', delete_user, name='delete'),
]