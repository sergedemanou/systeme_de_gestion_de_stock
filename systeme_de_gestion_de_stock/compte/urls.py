from django.urls import path
from . import views


urlpatterns = [
    path('inscription/', views.inscriptionPage, name='inscription'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]
