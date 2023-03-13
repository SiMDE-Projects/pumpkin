from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    #@action(detail=False, methods=['post'])
    #def my_view(self, request):
        # Traitement de la requête POST
        #return Response({'message': 'Requête POST traitée avec succès'})