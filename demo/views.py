from .models import Book
from rest_framework import viewsets
from .serializers import  BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,) # there might be multiple classes
    permission_classes = (IsAuthenticated,)

