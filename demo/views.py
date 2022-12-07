from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .models import Book
def first(request):
    return HttpResponse("frist message from views, hello world")

# access db by Book.objects.,  can be all, filter or get
class Another(View):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"we have {book.title} book in DB with ID {book.id}<br>"
    def get(self, request):
        return HttpResponse(self.output)
