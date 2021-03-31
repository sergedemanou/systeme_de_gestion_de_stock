from django.shortcuts import render
from .models import *
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def list_client(request,pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    myFilter=CommandeFiltre(request.GET,queryset=commande)
    commande=myFilter.qs

    context={'client': client, 'commande': commande, 'commande_total': commande_total, 'myFilter': myFilter }
    return render(request, 'client/list_client.html', context)

def supprimer_client(request,pk):
    client= Client.objects.get(id=pk)
    if request.method=='POST':
        client.delete()
        return redirect('/')
    context={'client':client}
    return render(request, 'client/supprimer_client.html',context)

def ajouter_client(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'client/ajouter_client.html',context)
