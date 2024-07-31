from django.urls import path
from .views import *


urlpatterns = [
    path('list_user/', ListUser.as_view(), name='list_user'),
    path('list_book/', list_book, name='list_book'),
]
