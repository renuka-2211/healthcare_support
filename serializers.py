from rest_framework import serializers
from .models import SupportRequest

class SupportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = '__all__'
