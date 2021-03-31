from django.forms import ModelForm
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model=Client
        fields='__all__'

    def __init__(self,*args, **kwargs):
        super(CommandeForm, self). __init__(*args, **kwargs)
        self.fields['nom'].required = False     
        self.fields['telephone'].required = False     
