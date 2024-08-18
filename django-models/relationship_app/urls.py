from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]



from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # Other URL patterns for your app
]

# Link the views
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

# # Define the URL patterns for the secured views
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('add-book/', views.add_book, name='add_book'),  # URL for adding a book
#     path('edit-book/<int:pk>/', views.edit_book, name='edit_book'),  # URL for editing a book
#     path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),  # URL for deleting a book
# ]

from django.urls import path
from .views import add_book, edit_book, delete_book, BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]