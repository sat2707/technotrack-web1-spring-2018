from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from users.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


@login_required
def all_users (request):
    users = User.objects.all()
    return render(request, 'users.html', {
        'users': users
    })


@login_required
def user (request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user.html', {
        'user': user
    })


def login_form(request):
    login_form = LoginForm()

    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

    return render(request, 'auth.html', {
        'login_form': login_form
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login/')