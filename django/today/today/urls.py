"""today URL Configuration

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
import todo.views
from todo import classviews as todoclassviews
from todo import usertodoclassviews as usertodoclassviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("rest/todos/", todo.views.todos),
    path("rest/todos/<int:id>", todo.views.todo_details),
    # REST class views
    path("restv2/todos/", todoclassviews.TodoList.as_view()),
    path("restv2/todos/<int:pk>", todoclassviews.TodoDetails.as_view()),

    # REST class views for UserTodo
    path("rest/usertodos/", usertodoclassviews.UserTodoList.as_view()),
]
