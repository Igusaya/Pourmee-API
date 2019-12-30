from PourmeeAPI.models import Card
from PourmeeAPI.serializers import CardSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CardList(APIView):
    """
    List all Card, or create a new card.
    """
    def get(self, request, format=None):
        card = Card.objects.all()
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
