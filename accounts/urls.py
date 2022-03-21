from django.urls import path
from django.conf import settings
from django.urls.conf import include


urlpatterns = [
    path('accounts/', include('allauth.urls')),
]