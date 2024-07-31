from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .pagination import CustomPagination
from django.contrib.auth.models import User
from main.models import Author, Book, Store
from .serialiser import UserSerialiser, BookSerialiser

@api_view(['GET'])
def list_book(request):
    '''
    To retrieve all the books from Book model.
    '''
    books = Book.objects.all()
    serialiser = BookSerialiser(books, many=True)
    return Response(serialiser.data, status=status.HTTP_200_OK)
    
    
    
class ListUser(generics.ListAPIView):
    '''
    To retrieve all the users from User model.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    pagination_class = CustomPagination
    
