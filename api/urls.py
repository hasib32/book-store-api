from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('users/', views.user_view.UserList.as_view()),
    path('users/<int:pk>', views.user_view.UserDetail.as_view()),
    path('users/me', views.user_view.AuthUserDetail.as_view()),

    path('library/', views.library_view.LibraryList.as_view()),
    path('library/<int:pk>', views.library_view.LibraryDetail.as_view()),

    path('books/', views.book_view.BookList.as_view()),
    path('books/<int:pk>', views.book_view.BookDetail.as_view()),

    path('library/<int:pk>/books', views.library_book_view.LibraryBookList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
