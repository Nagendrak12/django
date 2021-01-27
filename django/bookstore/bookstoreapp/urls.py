
from django.urls import path
from .import views,classviews,account_views

urlpatterns = [
  path("home/",views.home),
  path("list/",views.list_books),
  path("add/",views.add_book),
  path("edit/<int:id>/", views.edit_book),
  path("delete/<int:id>/", views.delete_book),
  path("search/", views.search_book),
  path("search_book/", views.search_book_form),
  path("listpublisher/",views.publisher_details),
  path("logout/", account_views.logout_user),
  path("login/", account_views.login_user),
    path("register/", account_views.register_user),
  path("rest/books/",classviews.BookList.as_view()),
  path("rest/books/<int:pk>",classviews.BookDetails.as_view()),
  

]
