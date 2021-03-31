from django.forms import ModelForm
from .models import Commande
from crispy_forms.helper import FormHelper

class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields='__all__'

    def __init__(self,*args, **kwargs):
        super(CommandeForm, self). __init__(*args, **kwargs)
        self.fields['client'].required = False     
        self.fields['produit'].required = False     
        self.fields['status'].required = False    

        # (self.fields nous permet d'enveler les asterices sur les formulaires de crispy forms) 
