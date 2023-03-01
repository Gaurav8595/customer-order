from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"