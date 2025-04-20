from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import FitUserCreationForm
from django.contrib.auth import get_user_model
#
from .forms import FitUserCreationForm
#
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


# Create your views here.
def signup(request):
    print("DEBUG: View loaded", request.method)

    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = FitUserCreationForm()
        #template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
                      {'template_data': template_data})

    elif request.method == 'POST':
        #form = FitUserCreationForm(request.POST)

        form = FitUserCreationForm(request.POST)
        print("DEBUG: Form submitted.")
        print("DEBUG: is_valid:", form.is_valid())
        print("DEBUG: form.errors:", form.errors)
        print("Form submitted. Is valid?", form.is_valid())
        print("Form errors:", form.errors)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            print("Form Errors:", form.errors)
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                      {'template_data': template_data})
            #return render(request, 'accounts/signup.html', {'template_data': template_data})


def login(request):
    template_data = {}

    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
                {'template_data': template_data})

    elif request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                  {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')


@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()

    return render(request, 'accounts/orders.html',
                  {'template_data': template_data})

def reset_password_username(request):
    template_data = {'title': 'Reset Password'}

    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/reset_password_username.html', {'template_data': template_data})
        FitModel = get_user_model()
        try:
            validate_password(new_password)
        except ValidationError as invalid:
            for msg in invalid.messages:
                messages.error(request, msg)
            return render(request, 'accounts/reset_password_username.html', {'template_data': template_data})
        try:
            user = FitModel.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password has been reset successfully. You can now log in.")
            list(messages.get_messages(request))
            return redirect('accounts.login')
        except FitModel.DoesNotExist:
            messages.error(request, "User not found.")

    return render(request, 'accounts/reset_password_username.html', {'template_data': template_data})