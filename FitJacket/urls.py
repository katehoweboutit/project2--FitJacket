from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('myFitness/', include('myFitness.urls')),
    path('eventsChallenges/', include('eventsChallenges.urls')),
    path('friends/', include('friends.urls')),
    path('exercise/', include('exercise.urls')),
]