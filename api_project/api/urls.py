from django.urls import path
from .views import BookListCreateView
from .views import BookList

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/', BookList.as_view(), name='book-list'),
]