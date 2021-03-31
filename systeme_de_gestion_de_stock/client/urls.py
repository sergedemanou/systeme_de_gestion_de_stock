from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk>/', views.list_client, name='client'),
    path('<str:pk>/', views.supprimer_client, name='supprimer_client'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
]
