from PourmeeAPI.models import Card
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'position', 'color', 'created']
