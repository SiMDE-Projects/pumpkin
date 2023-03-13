from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('nom', 'reference', 'etat', 'commentaire','quantite', 'date_achat','creation_date', 'updated_date')
