from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.register_student, name="register_student"),
    path('staff/', views.register_staff, name="register_staff"),
    path('non_member/', views.register_non_member, name="register_non_member"),

    # login 
    path('login/', views.signin, name="login"),
    path('logout/', views.logout_user, name="logout"),
]