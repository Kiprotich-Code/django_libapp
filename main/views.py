from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from librarian.models import Books, BooksBorrowed
from .forms import BorrowBooksForm, ContactForm, FeedbackForm

# Create your views here
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    context = {
        'form': form
    }    
    return render(request, 'index.html', context)

@login_required()
def staff_home(request):
    return render(request, 'main/staff_home.html')

@login_required()
def non_member_home(request):
    return render(request, 'main/non_member_home.html')

# STUDENT VIEWS
@login_required()
def student_home(request):
    return render(request, 'main/students/student_home.html')

def student_payments(request):
    return render(request, 'main/students/student_payments.html')

class BooksListView(ListView):
    context_object_name = 'books'
    model = Books
    template_name = 'main/students/student_books.html'
    paginate_by = 6


# Borrow 
def borrow_book(request, id):
    book = Books.objects.get(id=id)
    if request.method == 'POST':
        form = BorrowBooksForm(request.POST)
        if form.is_valid():
            frm = form.save(commit=False)
            frm.book = book
            frm.user = request.user
            frm.save()
            return redirect('borrowed_books')
        
    else:
        form = BorrowBooksForm()

    context = {
        'form': form,
        'book': book
    }
    return render(request, 'main/students/borrow_book.html', context)


def student_borrowed_books(request):
    borrowed_books = BooksBorrowed.objects.filter(user=request.user)
    context = {
        'borrowed_books': borrowed_books
    }
    return render(request, 'main/students/borrowed_books.html', context)

# Contact Views
# Contact Us 
def give_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('student_home')

    else:
        form = FeedbackForm()

    context = {
        'form': form
    }
    return render(request, 'main/students/give_feedback.html', context)


# Notifications