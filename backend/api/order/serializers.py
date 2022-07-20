from rest_framework import serializers

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from order.models import Order, OrderItems
from product.models import Product
from api.product.serializers import ProductOutSerializer

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["status", "total_price", "is_active"]

class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'product_price', 'qty']

class OrderCreateDocsSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)
    class Meta:
        model = Order
        fields = ['status', 'total_price', 'is_active', 'items']

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title_tm', 'title_ru', 'title_en', 'main_image', 'main_image_mobile',
                'is_active', 'is_usd']

class OrderItemsOutSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer(many=False)
    class Meta:
        model = OrderItems
        fields = ['id', 'product_price', 'product']

class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemsOutSerializer(many=True, source='order_products')
    class Meta:
        model = Order
        fields = ['id', 'status', 'total_price', 'is_active', 'created_at', 'updated_at', 'items']