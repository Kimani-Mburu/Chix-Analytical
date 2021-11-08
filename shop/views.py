from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = "shop/index.html"

class Cart(TemplateView):
    template_name = "shop/cart.html"