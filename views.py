from rest_framework import viewsets
from .models import SupportRequest
from .serializers import SupportRequestSerializer
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = SupportRequest.objects.all()
    serializer_class = SupportRequestSerializer

@api_view(['GET'])
def health_tip(request):
    response = requests.get("https://api.quotable.io/random")
    return Response(response.json())
