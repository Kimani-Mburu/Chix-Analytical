from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [path("", views.Home.as_view(), name="home"),
               path("cart/", views.Cart.as_view(), name="cart")]
