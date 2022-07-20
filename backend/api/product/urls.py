from django.urls import path

from . import views

urlpatterns = [
    path('product-list/', views.ProductListView.as_view(), name="product-list"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('design-samples/', views.SampleImageView.as_view(), name='design-samples'),
    path('design-samples-create/', views.SICreateView.as_view(), name='design-samples-create'),
    path('banners/', views.BannerListView.as_view(), name='banners'),
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
]