from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome to my show</h1>")
                       
                       