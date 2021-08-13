from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    dic = {
        "stds" : {
                "areesha" : "IT Eve",       
                "tahira" : "IT Eve",
                "noreen":  "IT MOR",
                "asia" : "IT EVE",
                "gull" : "IT EVE",
                "javaryia" : "IT MOR"
        },
        'teacher' : "Mamoona",
        "course" : "Django"
    }
    return render(request , "index.html" , dic)

def hello(request):
    return HttpResponse("<h1>I am a hello function</h1>")