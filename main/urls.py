from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('list_user/', ListUser.as_view(), name='list_user'),
]
