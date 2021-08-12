from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def hello(request):
    return HttpResponse("<h1>I am a hello function</h1>")