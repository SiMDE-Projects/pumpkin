from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('nom', 'reference', 'etat', 'commentaire','quantite', 'date_achat','creation_date', 'updated_date')


admin.site.register(Item, ItemAdmin)

