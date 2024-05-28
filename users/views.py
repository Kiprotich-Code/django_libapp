from django.shortcuts import render, redirect
from .forms import StudentRegisterForm, StaffRegisterForm, NonMemberRegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

# Create your views here.
def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'student'
            user.save()
            return redirect('login')
        
        
    else:
        form = StudentRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register_student.html', context)


def register_staff(request):
    if request.method == 'POST':
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'staff'
            user.save()
            return redirect('login')
        
    else:
        form = StaffRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register_staff.html', context)


def register_non_member(request):
    if request.method == 'POST':
        form = NonMemberRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'non_member'
            user.save()
            return redirect('login')
        
    else:
        form = NonMemberRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register_non_member.html', context)


# login
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            
            # redirect users based on roles
            if user.user_type == 'student':
                return redirect('student_home')
            
            elif user.user_type == 'staff':
                return redirect('staff_home')
            
            elif user.user_type == 'non_member':
                return redirect('non_member_home')
            
            elif user.is_staff:
                return redirect('dashboard')
            
        else:
            return redirect('login') 

    else:
        form = LoginForm()
    context = {
        'form': form
    }
        
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')