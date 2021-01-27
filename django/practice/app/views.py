from django.shortcuts import render,redirect
from app.forms import MovieForm
from app.models import Movies_Series

# Create your views here.

def login(request):
    return render(request,'login.html')


def add_movies(request):
    if request.method=='GET':
        f=MovieForm()
        return render(request,"add.html",{'form':f})
    else:
        f=MovieForm(request.POST)
        if f.is_valid():
            f.save()
            f=MovieForm()
            return render(request, "add.html", {'form': f, 'message': "added succesfully"})
        else:
            return render(request, "add.html", {'form': f, 'message': "sorry! couldn't added due to some error"})
    
