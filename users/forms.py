from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Create your forms here 
class StudentRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Enter Password'}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Confirm Password'}
    ))

    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'admission_no', 'password1', 'password2', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Email Address'}),
            'full_names': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Your Full Names'}),
            'admission_no': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Admission No'}),
        }

class StaffRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Enter Password'}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Confirm Password'}
    ))

    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'staff_id', 'password1', 'password2', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Email Address'}),
            'full_names': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Your Full Names'}),
            'staff_id': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Your Staff ID'}),
        }

class NonMemberRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Enter Password'}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'max-width: 600px', 'placeholder': 'Confirm Password'}
    ))

    class Meta():
        model = CustomUser
        fields = ['email', 'full_names', 'password1', 'password2', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Email Address'}),
            'full_names': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 600px', 'placeholder': 'Enter Your Full Names'}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' :'Email', 'style': 'max-width: 600px;'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'style': 'max-width: 600px;'
            }
        )
    )