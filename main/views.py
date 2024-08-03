from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .pagination import CustomPagination
from django.contrib.auth.models import User
from main.models import Author, Book, Store
from .serialiser import UserSerialiser, BookSerialiser, StoreSerialiser
from django.core.cache import cache

@api_view(['GET'])
def list_book(request):
    '''
    To retrieve all the books from Book model.
    cache added for books instances.
    '''
    books = cache.get('books')
    if not books:
        books = Book.objects.select_related('author').all()
        cache.set('books', books, timeout=60*15)
        print('books cache created.')
    serialiser = BookSerialiser(books, many=True)
    return Response(serialiser.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def list_store(request):
    '''
    To retrieve all the stores with book anme from Store model.
    cache added for books instances.
    '''
    stores = cache.get('stores')
    if not stores:
        stores = Store.objects.prefetch_related('book').all()
        cache.set('stores', stores, timeout=60*15)
        print('stores cache created..')
    serialiser = StoreSerialiser(stores, many=True)
    return Response(serialiser.data, status=status.HTTP_200_OK)
    
    
    
class ListUser(generics.ListAPIView):
    '''
    To retrieve all the users from User model.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    pagination_class = CustomPagination
    
