import io
import json

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from accounts.models import FitUser
from accounts.forms import FitUserCreationForm

@csrf_exempt
def add_friend(request):
    template_data = {}
    template_data['title'] = 'Friends'
    users = FitUser.objects.exclude(username=request.user.username)
    template_data['users'] = users
    if request.method == 'GET':
        search_term = request.GET.get('search')
        if search_term:
        # show all friends with that in name
            users = FitUser.objects.filter(first_name__icontains=search_term)
            users_last = FitUser.objects.filter(last_name__icontains=search_term)
            users_name = FitUser.objects.filter(username__icontains=search_term)
            users = users.union(users_last)
            users = users.union(users_name)
        else:
            users = FitUser.objects.exclude(Q(username=request.user.username) | Q(username=""))
        template_data['users'] = users
        return render(request, 'friends/addfriend.html',
                      {'template_data': template_data})
    elif request.method == 'POST':
        first = request.POST.get('username')
        friend = FitUser.objects.filter(Q(username=first)).first()
        current_user = FitUser(request.user)
        #strio = io.StringIO(current_user.friends)
        try :
            #jlist = json.load(strio)
            jlist = json.loads(request.user.friends)
        except json.decoder.JSONDecodeError:
            jlist = []
        if friend:
            jlist.append(friend.username)
            request.user.friends = json.dumps(jlist)
            request.user.save(update_fields=['friends'])
        #return render(request, 'friends/index.html', {'template_data' : template_data})
        return index(request)

def index(request):
    #List of all current friends from database
    # find out how to get the current user, then reference their list of friends (from a database)
    template_data = {}
    template_data['title'] = 'Friends'
    if request.user.friends:
        friends = json.loads(request.user.friends)
        fri = FitUser.objects.filter(Q(username=" "))
        for friend in friends:
            fri = fri.union(FitUser.objects.filter(Q(username=friend)))
        template_data['friends'] = fri
        template_data['friends'] = fri.order_by('-fit_points')
    else:
        template_data['friends'] = []
    return render(request, 'friends/index.html',
                  {'template_data': template_data})

