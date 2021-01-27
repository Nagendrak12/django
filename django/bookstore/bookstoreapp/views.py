from django.shortcuts import render,redirect
from .models import Book,Publisher
from django.db.models import Sum, Count
from .forms import BookForm, PublisherForm
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    summary = Book.objects.all().aggregate(
        total=Sum('price'), count=Count('id'))
    return render(request, 'home.html', {'summary': summary})

@login_required
def list_books(request):
    return render(request, 'list.html',
                  {'book': Book.objects.all()})
    

@login_required
def add_book(request):
    if request.method == 'GET':
        f = BookForm()
        return render(request, 'add.html', {'form': f})
    else:
        f = BookForm(request.POST)
        if f.is_valid():
            f.save()  # Insert row into table
            f = BookForm()
            return render(request, 'add.html',
                          {'form': f, 'message': "Added Successfully!"})
        else:
            return render(request, 'add.html',
                          {'form': f, 'message': "Sorry! Could not add due to error!"})
    

@login_required
def edit_book(request, id):
    if request.method == 'GET':
        try:
            exp = Book.objects.get(id=id)  # Take data from DB
            form = BookForm(instance=exp)
            return render(request, 'edit.html', {'form': form})
        except ObjectDoesNotExist:
            return render(request, 'edit.html',
                          {'message': 'Book Id Not Found!'})
    else:
        exp = Book.objects.get(id=id)
        form = BookForm(instance=exp, data=request.POST)
        if form.is_valid():
            form.save()  # Update database

            return redirect("/bookstore/list/")
        else:
            return render(request, 'edit.html', {'form': form})


@login_required
def delete_book(request, id):
    try:
        exp = Book.objects.get(id=id)
        exp.delete()
        return redirect("/bookstore/list/")
    except Exception as ex:
        return render(request, 'delete.html', {'message': ex})


@login_required
def search_book(request):
    name = request.GET['name']
    entries = Book.objects.filter(
        title__contains=name)
    dict_entries = list(entries.values())
    response = JsonResponse(dict_entries, safe=False)
    response.set_cookie("searchstring", name, expires=datetime.datetime.now() +
                        datetime.timedelta(days=10))
    return response


@login_required
def search_book_form(request):
    if 'searchstring' in request.COOKIES:
        searchstring = request.COOKIES['searchstring']
    else:
        searchstring = ''
    return render(request, 'search.html', {'searchstring': searchstring})


@login_required
def publisher_details(request):
    return render(request, 'publisher.html',
                  {'publisher': Publisher.objects.all()})

