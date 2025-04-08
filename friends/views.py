from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import FitUser

def add_friend(request):
    search_term = request.GET.get('search')
    if search_term:
        # show all friends with that in name

        users = FitUser.objects.filter(first_name__icontains=search_term)
        users_last = FitUser.objects.filter(last_name__icontains=search_term)
        users = users.union(users_last)
    else:
        users = FitUser.objects.all()
    template_data = {}
    template_data['title'] = 'Friends'
    template_data['users'] = users
    return render(request, 'friends/addfriend.html',
                  {'template_data': template_data})
def index(request):
    #List of all current friends from database
    # find out how to get the current user, then reference their list of friends (from a database)
    template_data = {}
    template_data['title'] = 'Friends'
    return render(request, 'friends/index.html',
                  {'template_data': template_data})
