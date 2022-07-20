from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),
    path('register/', views.registerUser, name="register"),
    path('profile-create/', views.ProfileCreateView.as_view(), name="profile-create"),
    path("profile-delete/<int:pk>/", views.ProfileDelete.as_view(), name="profile-delete")
]