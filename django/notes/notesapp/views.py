from django.shortcuts import render,redirect
from notesapp.models import MyNotes
from django.db.models import Count
from .forms import MyNotesForm,MyNotesEditForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    user = request.user
    summary = MyNotes.objects.filter(user=user).aggregate(count=Count('id'))
    return render(request, 'home.html', {'summary': summary})


@login_required
def list_notes(request):
    return render(request, 'view_notes.html',
                  {'mynotes': MyNotes.objects.filter(user=request.user).order_by("-updated_on")})


@login_required
def list_recent_notes(request):
    return render(request, 'view_notes.html',
                  {'mynotes': MyNotes.objects.filter(user=request.user).order_by("-updated_on")[:5]})


@login_required
def add_note(request):
    if request.method == 'GET':
        f = MyNotesForm()
        return render(request, 'add_notes.html', {'form': f})
    else:
        f = MyNotesForm(request.POST)
        if f.is_valid():
            exp = f.save(commit=False)
            exp.user = request.user
            exp.save()
            f = MyNotesForm()  # Create empty form
            return render(request, 'add_notes.html',
                          {'form': f, 'message': "Added Successfully!"})
        else:
            return render(request, 'add_notes.html',
                          {'form': f, 'message': "Sorry! Could not add due to error!"})


@login_required
def edit_note(request, id):
    if request.method == 'GET':
        try:
            exp = MyNotes.objects.get(id=id)  # Take data from DB
            form = MyNotesEditForm(instance=exp)
            return render(request, 'edit_note.html', {'form': form})
        except ObjectDoesNotExist:
            return render(request, 'edit_note.html',
                          {'message': 'Expenditure Id Not Found!'})
    else:
        exp = MyNotes.objects.get(id=id)
        form = MyNotesEditForm(instance=exp, data=request.POST)
        if form.is_valid():
            form.save()  # Update database
            return redirect("/list/")
        else:
            return render(request, 'edit_note.html', {'form': form})


@login_required
def delete_note(request, id):
    try:
        exp = MyNotes.objects.get(id=id)
        exp.delete()
        return redirect("/list/")
    except Exception as ex:
        return render(request, 'delete_note.html', {'message': ex})


def search_note(request):
    desc = request.GET['desc']
    entries = MyNotes.objects.filter(
        user=request.user,title__icontains=desc).order_by('-updated_on')
    dict_entries = list(entries.values())
    response = JsonResponse(dict_entries, safe=False)
    response.set_cookie("searchstring", desc, expires=datetime.datetime.now() +
                        datetime.timedelta(days=10))
    return response


def search_note_form(request):
    if 'searchstring' in request.COOKIES:
        searchstring = request.COOKIES['searchstring']
    else:
        searchstring = ''
    return render(request, 'master.html', {'searchstring': searchstring})
