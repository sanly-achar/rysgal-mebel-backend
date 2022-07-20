from django.db import models
from api.utils import get_random_string
from django.contrib.auth.models import User

class Settings(models.Model):
    course = models.FloatField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.course) + str(self.created_at)

def general_image(instance, filename):
    rand = get_random_string()
    return 'general/{rand}-{filename}'.format(rand=rand, filename=filename)

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=general_image, default='general/default.jpg')
    image_mobile = models.ImageField(upload_to=general_image, default='general/default.jpg')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SampleImages(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=general_image, default='general/default.jpg')
    image_mobile = models.ImageField(upload_to=general_image, default='general/default.jpg')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=general_image, default='general/default.jpg')
    image_mobile = models.ImageField(upload_to=general_image, default='general/default.jpg')

    def __str__(self):
        return self.title_tm

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_sub')
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_tm = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_tm

class Brand(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=general_image, default='general/default.jpg')

    def __str__(self):
        return self.title

def product_image(instance, filename):
    rand = get_random_string()
    return 'products/{rand}-{filename}'.format(rand=rand, filename=filename)

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, 
            null=True, blank=True, related_name='subcategory_product')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,
            null=True, blank=True)
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    main_image = models.ImageField(upload_to=product_image, default='products/default.jpg')
    main_image_mobile = models.ImageField(upload_to=product_image, default='products/default.jpg')
    description_tm = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    is_usd = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_tm

    def get_price(self):
        course = Settings.objects.latest('id')
        usd_price = round(float(self.price * course.course))
        if self.is_usd == True:
            return usd_price
        else:
            return self.price

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
            related_name='product_image')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=product_image, default='products/default.jpg')
    image_mobile = models.ImageField(upload_to=product_image, default='products/default.jpg')

    def __str__(self):
        return self.title

class Attribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attribute')
    title_tm = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_tm = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title_tm

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
            related_name='user_comment')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
            related_name='product_comment')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title