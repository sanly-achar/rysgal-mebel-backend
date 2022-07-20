from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

from product.models import (Settings, Banner, Category, SubCategory, Brand, Product,
        Images, Attribute, Comments, SampleImages)

class ProductListView(APIView, LimitOffsetPagination):
    param1 = openapi.Parameter('title', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    param2 = openapi.Parameter('byprice', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param3 = openapi.Parameter('bycreated', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param4 = openapi.Parameter('is_special', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    param5 = openapi.Parameter('liked', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)
    param6 = openapi.Parameter('category', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(manual_parameters=[param1, param2, param3, param4, param5, param6],
            operation_description="***IMPORTANT***: 'byprice' and 'bycreated' should not be used together\n***IMPORTANT***: 'liked' should be list of ids comma saparated. ex: ?liked=21,22,23",
            responses={200: ProductOutSerializer})
    def get(self, request):
        title = request.query_params.get('title', None)
        byprice = request.query_params.get('byprice', None)
        bycreated = request.query_params.get('bycreated', None)
        is_special = request.query_params.get('is_special', None)
        liked = request.query_params.get('liked', None)
        category = request.query_params.get('category', None)
        if byprice == 'true':
            byprice = True
        if byprice == 'false':
            byprice = False
        if bycreated == 'true':
            bycreated = True
        if bycreated == 'false':
            bycreated = False
        if is_special == 'true':
            is_special = True
        if is_special == 'false':
            is_special = False
        dliked = []
        if liked:
            liked = liked.split(',')
            for l in liked:
                if l.isdecimal():
                    dliked.append(int(l))

        try:
            products = Product.objects.filter(is_active=True)
            if title:
                products = products.filter(title__icontains=title)
            if category:
                products = products.filter(subcategory=category)
            if is_special == True:
                products = products.filter(is_special=is_special)
            if is_special == False:
                products = products.filter(is_special=is_special)
            if byprice == True:
                products = sorted(products, key=lambda p: p.get_price())
            if byprice == False:
                products = sorted(products, key=lambda p: p.get_price(), reverse=True)
            if bycreated == True:
                products = products.order_by('created_at')
            if bycreated == False:
                products = products.order_by('-created_at')
            if len(dliked) > 0:
                products = products.filter(pk__in=dliked)
            
            data = self.paginate_queryset(products, request, view=self)
            serializer = ProductOutSerializer(data, many=True)
            response = self.get_paginated_response(serializer.data)
            return Response({"response": "success", "data": response.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    @swagger_auto_schema(responses={200: ProductDetailSerializer})
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductDetailSerializer(product)
            print(product.subcategory.id)
            cat_id = product.subcategory.id
            cat_products = Product.objects.filter(subcategory=cat_id).exclude(id=product.id)[:8]
            # cat_products = cat_products.exclude(id=product.id)
            spserializer = ProductOutSerializer(cat_products, many=True)
            return Response({"response": "success", "data": serializer.data, "similar_products":spserializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class SampleImageView(APIView):
    @swagger_auto_schema(responses={200: SampleImageSerializer})
    def get(self, request):
        try:
            samples = SampleImages.objects.filter(is_active=True)[:4]
            serializer = SampleImageSerializer(samples, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)
    

class SICreateView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]
    @swagger_auto_schema(request_body=SampleImageSerializer, responses={200: SampleImageSerializer})
    def post(self, request):
        try:
            data = request.data
            serializer = SampleImageInSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)


class BannerListView(APIView):
    @swagger_auto_schema(responses={200: BannerListSerializer})
    def get(self, request):
        try:
            banners = Banner.objects.filter(is_active=True)[:3]
            serializer = BannerListSerializer(banners, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class BrandListView(APIView):
    @swagger_auto_schema(responses={200: BrandSerializer})
    def get(self, request):
        try:
            brands = Brand.objects.all()
            serializer = BrandSerializer(brands, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST)

class CategoryListView(APIView):
    @swagger_auto_schema(responses={200:CategoryListSerializer})
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategoryListSerializer(categories, many=True)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({'response':'error'}, status=status.HTTP_400_BAD_REQUEST) 