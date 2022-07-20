from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    STATUS = [
        ('ORDERPLACED', 'ORDERPLACED'),
        ('ACCEPTED', 'ACCEPTED'),
        ('DECLINED', 'DECLINED'),
        ('SHIPPED', 'SHIPPED'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNED', 'RETURNED'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    status = models.CharField(max_length=64, choices=STATUS, default='ORDERPLACED')
    total_price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username) + '-' + str(self.total_price)

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,related_name='product_orders')
    product_price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product.title_tm) + '-' + str(self.order.user.username)