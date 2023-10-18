from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request: HttpRequest):
    # return HttpResponse("Hello World")
    res = range(1, 15)
    return render(request, "todo/home.html", {"todos": res})
