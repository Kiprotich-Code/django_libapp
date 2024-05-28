from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('staff_home/', views.staff_home, name="staff_home"),
    path('non_member_home/', views.non_member_home, name="non_member_home"),

    # students urls 
    path('student_home/', views.student_home, name="student_home"),
    path('student_payments/', views.student_payments, name="student_payments"),
    path('student_books/', views.BooksListView.as_view(), name="student_books"),
    path('borrow_book/<id>', views.borrow_book, name="borrow_book"),
    path('borrowed_books/', views.student_borrowed_books, name="borrowed_books"),


    # contact 
    path('give_feedback/', views.give_feedback, name="give_feedback"),
]