from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        return Response({'status': 200, 'message': 'Hello DRF from GET'})
    if request.method == 'POST':
        return Response({'status': 200, 'message': 'Hello DRF from POST'})
    
