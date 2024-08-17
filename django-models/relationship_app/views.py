from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Library, Book  # Ensure you're importing the models

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a homepage or another page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Function to check if user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view
@user_passes_test(is_admin, login_url='/login/')  # Redirect to login if not admin
def admin_view(request):
    return render(request, 'admin_view.html')
