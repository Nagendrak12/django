from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.shortcuts import redirect, render


def logout_user(request):
    logout(request)
    return redirect("/login/")


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
            return redirect("/home/")


def register_user(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'register.html', {'form': form})


def change_password_user(request):
    if request.method == 'GET':
        form = PasswordChangeForm(request.user.password)
        return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            update_session_auth_hash(request, user)
            return redirect('/home/')
        else:
            return render(request, 'change_password.html', {'form': form, 'messages': 'not changed'})
