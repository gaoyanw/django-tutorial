from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
def first(request):
    return HttpResponse("frist message from views, hello world")

class Another(View):
    def get(self, request):
        return HttpResponse("This is another function inside class, hello world")
