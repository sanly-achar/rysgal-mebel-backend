from rest_framework import serializers

from product.models import (Settings, Banner, Category, SubCategory, Brand, Product,
        Images, Attribute, Comments, SampleImages)

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", 'title_tm', 'title_ru', 'title_en', 'main_image', 'main_image_mobile', 
                'description_tm', 'description_ru', 'description_en','get_price', 'is_special', 'created_at']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class SampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleImages
        fields = '__all__'

class SampleImageInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleImages
        # fields = ['id', 'image', 'image_mobile']
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    image_list = ProductImageSerializer(many=True, source='product_image')
    attributes = ProductAttributeSerializer(many=True, source='product_attribute')
    comments = ProductCommentSerializer(many=True, source='product_comment')
    subcategory = SubCategorySerializer(many=False)
    brand = BrandSerializer(many=False)
    class Meta:
        model = Product
        fields = ['id', 'title_tm', 'title_ru', 'title_en', 'main_image', 'main_image_mobile', 
                'description_tm', 'description_ru', 'description_en', 'price', 'is_usd', 'is_special', 'subcategory', 'brand', 
                'image_list', 'attributes', 'comments']

class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    subcategories=CategorySerializer(many=True, source="category_sub")
    class Meta:
        model = Category
        fields = ['id', 'title_tm', 'title_ru', 'title_en', 'image', 'image_mobile', 'subcategories']