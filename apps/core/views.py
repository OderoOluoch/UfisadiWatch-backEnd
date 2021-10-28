import random 
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.product.models import Product 
from apps.product.serializers import ProductSerializer
from rest_framework.views import APIView 

from .models import User 


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    # permission_classes = [permission.IsAuthenticatedORReadOnly] -> TODO DRF permissions
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,  status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def productDelete(request, pk):
    product = Product.objects.get(pk=pk)

    # TODO
    # -> on_delete, set following status : is_active=False, is_published=False, deleted_by=request.user etc.
    product.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


class UserApiView(APIView):
    def get(self, _):
        users = User.objects.all()

        # get random user
        user = random.choice(users)

        return Response({
            "id": user.id
            })


