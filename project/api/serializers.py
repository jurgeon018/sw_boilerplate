from rest_framework import serializers
from ..models import * 


class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser 
        exclude = []

