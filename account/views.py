from django.http.response import HttpResponse
from django.shortcuts import render


def sign_up(request):
    return render(request, "account/signup.html")
