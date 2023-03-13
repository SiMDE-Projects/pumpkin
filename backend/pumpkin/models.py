from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime




# Create your models here.
class Item(models.Model):

    class State(models.IntegerChoices):
        NEW = 1,"Neuf"
        GOOD = 2,"Bon"
        AVERAGE = 3,"Moyen"
        ACCEPTABLE = 4,"Acceptable"
        BAD = 5,"Mauvais"
        VERY_BAD = 6,"Très Mauvais"



    nom = models.CharField(max_length=60)
    reference = models.CharField(max_length=60)
    etat = models.IntegerField(max_length=25, choices=State.choices, default=1)
    commentaire = models.TextField(blank=True)
    quantite = models.IntegerField(validators=[MinValueValidator(1)])
    date_achat = models.DateField(default=None, null=True, blank=True)
    creation_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    updated_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))


    def _str_(self):
        return self.nom
