from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Laptop, Category
from .serializers import LaptopSerializer, CategorySerializer

class ListCategory(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        serializer_data = {
            'category': serializer.data,
            'status': 'success'
        }
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListLaptop(APIView):
    def get(self, request):
        laptops = Laptop.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        serializer_data = {
            'data': serializer.data,
            'status': 'success'
        }
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LaptopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailLaptop(APIView):
    def get(self, request, pk):
        laptop = get_object_or_404(Laptop, id=pk)
        serializer = LaptopSerializer(laptop)
        serializer_data = {
            'data': serializer.data,
            'status': 'success'
        }
        return Response(serializer_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        laptop = get_object_or_404(Laptop, id=pk)
        serializer = LaptopSerializer(laptop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        laptop = get_object_or_404(Laptop, id=pk)
        laptop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
