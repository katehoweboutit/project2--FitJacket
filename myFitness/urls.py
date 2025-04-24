from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='myFitness.index'),
    path('myFitness.listofDeath', views.index, name='myFitness.listofDeath'),
    path('myFitness.randoList', views.index, name='myFitness.randoList'),
]