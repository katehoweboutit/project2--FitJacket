from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='myFitness.index') #test comment TODO remove
]