from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .pagination import CustomPagination
from django.contrib.auth.models import User
from .serialiser import UserSerialiser

@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response({'status': 200, 'message': 'Hello DRF from GET'})
    if request.method == 'POST':
        return Response({'status': 200, 'message': 'Hello DRF from POST'})
    
class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    pagination_class = CustomPagination
    
