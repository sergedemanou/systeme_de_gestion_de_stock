import django_filters
from .models import Commande

class CommandeFiltre(django_filters.FilterSet):
    class Meta:
        model=Commande
        fields='__all__'
        exclude=['client','date_creation']

        # "exclude" permet d'exclure les champs qu'on ne veut pas qu'ils soient affichés