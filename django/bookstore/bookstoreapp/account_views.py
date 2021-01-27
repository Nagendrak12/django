from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_user(request):
    logout(request)
    return redirect("/bookstore/login/")


def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        user = authenticate(request, username=username,
                            password=request.POST['password'])
        if user is None:
            return render(request, 'login.html',
                          {'username': username, 'message': 'Invalid Login'})
        else:
            login(request, user)
            return redirect("/bookstore/home/")


def register_user(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/bookstore/home/')
        else:
            return render(request, 'register.html', {'form': form})