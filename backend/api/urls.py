from django.urls import path, include


urlpatterns = [
    path("products/", include("api.product.urls")),
    path('auth/', include('api.auth.urls')),
    path('order/', include('api.order.urls')),
]