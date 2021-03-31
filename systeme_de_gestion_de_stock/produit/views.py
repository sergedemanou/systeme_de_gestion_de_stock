from django.shortcuts import render
from commande.models import *
from client.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# le decorateur @login_required permet aux clients de se logger avant d'acceder à la page d'accueil
@login_required(login_url='login')
def home(request):
    commandes = Commande.objects.all
    clients = Client.objects.all
    context ={
        'commandes': commandes,
        'clients': clients
    }
    return render(request, 'produit/accueil.html', context)