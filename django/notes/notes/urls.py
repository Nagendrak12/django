"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notesapp import views,account_views
from notesapp import usernotesclassviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.home),
    path("list/",views.list_notes),
    path("add/",views.add_note),
    path("edit/<int:id>",views.edit_note),
    path("delete/<int:id>",views.delete_note),
    path("recent/",views.list_recent_notes),
    path("search_note/", views.search_note),
    path("search/", views.search_note_form),
    path("logout/", account_views.logout_user),
    path("login/", account_views.login_user),
    path("register/", account_views.register_user),
    path("changepwd/", account_views.change_password_user),
    path("usermynotes_rest/", usernotesclassviews.MyNotesList.as_view()),
    path("usermynotes_rest/<int:pk>/", usernotesclassviews.MyNotesDetails.as_view()),
]
