from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreerUtilisateur
from django.contrib import messages
# Create your views here.
def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method =='POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Compte crée avec succès pour ' + user + ' !')
            return redirect('login')
    context={'form': form}
    return render(request, 'compte/inscription.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Utilisateur ou mot de passe incorrect")
    context={}
    return render(request, 'compte/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')
