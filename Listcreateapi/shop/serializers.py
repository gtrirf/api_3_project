from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100)
    # price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # description = serializers.CharField(max_length=100)
    # image=serializers.ImageField()

    class Meta:
        model = Product
        fields = '__all__'
