from django.urls import path

from . import views

urlpatterns = [
    path('order-list/', views.OrderListView.as_view(), name="order-list"),
    path('order-detail/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order-create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order-update/<int:pk>/', views.OrderUpdateView.as_view(), name="order-update"),
    path('order-delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-detelete'),
]