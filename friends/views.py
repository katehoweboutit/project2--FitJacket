from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import FitUser

def add_friend(request):
    template_data = {}
    template_data['title'] = 'Friends'
    if request.method == 'GET':
        search_term = request.GET.get('search')
        if search_term:
        # show all friends with that in name
            users = FitUser.objects.filter(first_name__icontains=search_term)
            users_last = FitUser.objects.filter(last_name__icontains=search_term)
            users = users.union(users_last)
        else:
            users = FitUser.objects.all()
        template_data['users'] = users
        return render(request, 'friends/addfriend.html',
                      {'template_data': template_data})
    else:
        #friend = FriendForm(request.POST)
        friend = FitUser.objects.filter(Q(first_name=request.POST.get('first')) | Q(last_name=request.POST.get('last')))
        current_user = request.user
        FitUser(current_user).friends.add(friend)
        return render(request, 'friends/index.html', {'template_data' : template_data})

def index(request):
    #List of all current friends from database
    # find out how to get the current user, then reference their list of friends (from a database)
    template_data = {}
    template_data['title'] = 'Friends'
    current_user = request.user
    template_data['friends'] = FitUser(current_user).friends
    return render(request, 'friends/index.html',
                  {'template_data': template_data})
