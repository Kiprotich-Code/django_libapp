from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.admin_dashboard, name="dashboard"),
    path('add_books/', views.add_books, name="add_books"),
    path('payments/', TemplateView.as_view(template_name="librarian/payments.html"), name="payments"),

    # cbv's 
    path('books/', views.BooksListView.as_view(), name="books"),
    path('book_details/<pk>', views.BookDetailView.as_view(), name="book_details"),
    path("update_book/<pk>", views.BookUpdateView.as_view(), name="update_book"),
    path('<pk>/delete/', views.BookDeleteView.as_view(), name="delete_book"),

    # Borrowed books
    path('all_borrowed_books/', views.BorrowedBooksList.as_view(), name="all_borrowed_books"),
    path('/books/<int:book_id>/approve/', views.approve_request, name="approve_book_request"),
    path('/books/<int:book_id>/reject/', views.reject_request, name="reject_book_request"),

    # Book Return 
    path('book_return/', views.book_return_list, name="book_return"),
    path('/books/<int:book_id>/return/', views.confirm_book_return, name="confirm_book_return"),


    # Notifications 
    path('user_contacts/', views.user_contacts, name="user_contacts"),
    path('feedbacks/', views.feedbacks, name="feedbacks"),
]