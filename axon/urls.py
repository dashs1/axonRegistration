from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "axon"

urlpatterns = [
    path("", views.home_view, name="home-view"),
    path(r'login/', LoginView.as_view(), name='login' ),
    path(r'logout/', views.logout_view, name="logout" ),
]
