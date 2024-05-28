from django.shortcuts import render, redirect, get_object_or_404
from . models import Books, BooksBorrowed
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import AddBookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, HttpRequest
from main.models import Contact, Feedback

# Create your views here.
@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'librarian/dashboard.html')

# CRUD - BOOKS 
# Create 
@login_required(login_url="login")
def add_books(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')

    else:
        form = AddBookForm()

    context = {
        'form': form
    }
    return render(request, 'librarian/add_books.html', context)

class BooksListView(ListView):
    context_object_name = 'books'
    model = Books
    template_name = 'librarian/books.html'
    paginate_by = 5


class BookDetailView(DetailView):
    context_object_name = 'book'
    model = Books
    template_name = 'librarian/book_details.html'


class BookUpdateView(UpdateView):
    template_name = 'librarian/update_books.html'
    model = Books
    fields = ('title', 'department', 'ISBN', 'author', 'year_published', 'copies',)
    success_url = '/librarian/books/'


class BookDeleteView(DeleteView):
    model = Books
    success_url = '/librarian/books/'
    template_name = "librarian/confirm_delete_book.html"


# Book Borrowing 
class BorrowedBooksList(ListView):
    context_object_name = 'books'
    model = BooksBorrowed
    template_name = 'librarian/all_borrowed_books.html'
    paginate_by = 10

def approve_request(request: HttpRequest, book_id: int):
    try:
        # Fetch the BooksBorrowed instance based on the related book's ID and status "pending"
        book_borrowed = get_object_or_404(BooksBorrowed, book_id=book_id, status='pending')
        book_borrowed.status = "approved"
        book_borrowed.book.copies -= 1
        book_borrowed.book.save()
        book_borrowed.save()  # Save the changes to the database
        messages.success(request, "Book request has been approved")

    except Http404:
        messages.success(request, "No pending request to approved!")

    return redirect('all_borrowed_books')


def reject_request(request, book_id):
    try:
        book_borrowed = get_object_or_404(BooksBorrowed, book_id=book_id, status='pending')
        book_borrowed.status = "rejected"
        book_borrowed.save()  # Save the changes to the database
        messages.success(request, "Book request has been approved")

    except Http404:
        messages.success(request, "No pending request to approved!")        

    return redirect('all_borrowed_books')


# Book Return 
def book_return_list(request):
    books_borrowed = BooksBorrowed.objects.filter(status="approved")
    context = {
        'books_borrowed': books_borrowed
    }

    return render(request, 'librarian/book_return.html', context)


def confirm_book_return(request: HttpRequest, book_id: int):
    try:
        # Fetch the BooksBorrowed instance based on the related book's ID and status "pending"
        book_borrowed = get_object_or_404(BooksBorrowed, book_id=book_id, status='approved')
        book_borrowed.status = "returned"
        book_borrowed.book.copies += 1
        book_borrowed.book.save()
        book_borrowed.save()  # Save the changes to the database
        messages.success(request, "Book request has been returned")

    except Http404:
        messages.success(request, "No pending request to approved!")

    return redirect('book_return')


# Admin - Nofications 
# User Contact Us 
def user_contacts(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'librarian/contacts.html', context)

def feedbacks(request):
    feedbacks = Feedback.objects.all()

    context = {
        'feedbacks': feedbacks
    }

    return render(request, 'librarian/feedbacks.html', context)
