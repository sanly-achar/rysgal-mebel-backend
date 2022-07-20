from django.contrib import admin
from django.utils.html import format_html

from .models import (Settings, Banner, Category, SubCategory, Brand, Product,
        Images, Attribute, Comments, SampleImages)

class SettingsAdmin(admin.ModelAdmin):
        list_display = ['course', 'created_at']
        # list_editable = ['course']

class BannerAdmin(admin.ModelAdmin):
        def image_tag(self, obj):
                return format_html('<img src="{0}" style="width: 45px; height:45px;">'.format(obj.image.url))
        list_display = ['image_tag','title']

class SampleImagesAdmin(admin.ModelAdmin):
        def image_tag(self, obj):
                return format_html('<img src="{0}" style="width: 45px; height:45px;">'.format(obj.image.url))
        list_display = ['image_tag', 'title']

admin.site.register(Settings, SettingsAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(SampleImages,SampleImagesAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Attribute)
admin.site.register(Comments)