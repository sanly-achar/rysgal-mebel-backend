from itertools import count
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import *

from order.models import Order, OrderItems


class OrderListView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="***IMPORTANT***: Need pass bearer token as authentication.",
            responses={200: OrderSerializer})
    def get(self, request):
        try:
            user = request.user.id
            orders = Order.objects.filter(user=user)
            serializer = OrderSerializer(orders, many=True)
            return Response({"response": "success", "data": serializer.data}, 
                status=status.HTTP_200_OK)
        except:
            return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="***IMPORTANT***: Need pass bearer token as authentication.",
            responses={200: OrderSerializer})
    def get(self, request, pk):
        user = request.user.id
        order = Order.objects.get(pk=pk)
        if order.user.id != user:
            return Response({"response":"error", "message": "You do not have access to this data."}, status=status.HTTP_403_FORBIDDEN)
        serializer = OrderDetailSerializer(order)
        return Response({"response": "success", "data": serializer.data}, 
            status=status.HTTP_200_OK)

class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=OrderCreateDocsSerializer, responses={200: OrderSerializer})
    def post(self, request):
        user = request.user.id
        data = request.data
        data['user'] = user
        serializer = OrderSerializer(data=data)
        items = data['items']
        items_total = 0
        if len(items) > 0:
            for item in items:
                items_total += float(item['product_price']) * float(item['qty'])
        data['total_price'] = items_total
        if serializer.is_valid():
            serializer.save()
            for item in items:
                item['order'] = serializer.data['id']
                item_serializer = OrderItemsSerializer(data=item)
                if item_serializer.is_valid():
                    item_serializer.save()
                else:
                    return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)

class OrderUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=OrderUpdateSerializer, responses={200: OrderSerializer})
    def put(self, request, pk):
        user = request.user.id
        data = request.data
        order = Order.objects.get(pk=pk)
        if order.user.id != user:
            return Response({"response":"error", "message": "You not allowed to update this data."}, 
                    status=status.HTTP_403_FORBIDDEN)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)

class OrderDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            user = request.user.id
            order = Order.objects.get(pk=pk)
            if order.user.id != user:
                return Response({"response":"error", "message": "You not allowed to update this data."}, 
                        status=status.HTTP_403_FORBIDDEN)

            order.delete()
            return Response({"response": "success"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)

