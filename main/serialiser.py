from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Author, Book, Store

class UserSerialiser(serializers.ModelSerializer):
    '''
    To serialize all the users from User model.
    '''
    class Meta:
        model = User
        fields = ['username']


class AuthorSerialiser(serializers.ModelSerializer):
    '''
    To serialize all the authors from Author model.
    '''
    class Meta:
        model = Author
        fields = '__all__'

class BookSerialiser(serializers.ModelSerializer):
    '''
    To serialize all the books from Book model.
    '''
    author_name = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']