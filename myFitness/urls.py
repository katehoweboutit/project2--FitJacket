from django.urls import path
from . import views

urlpatterns = [
    path('data/<int:id>', views.data, name='myFitness.data'),
    path('', views.index, name='myFitness.index'),
    # path('myFitness.randoList', views.index, name='myFitness.randoList'),
]