from django.shortcuts import render, redirect
from .forms import CommandeForm
from .models import Commande
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def list_commande(request):
    return render(request, 'commande/list_commande.html')

@login_required(login_url='login')
def ajouter_commande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'commande/ajouter_commande.html',context)

@login_required(login_url='login')
def modifier_commande(request,pk):
    commande= Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'commande/ajouter_commande.html',context)

@login_required(login_url='login')
def supprimer_commande(request,pk):
    commande= Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request, 'commande/supprimer_commande.html',context)

@login_required(login_url='login')
def les_commandes(request):
    commandes = Commande.objects.all
    context={}
    return render(request, 'commande/les_commandes.html', context)