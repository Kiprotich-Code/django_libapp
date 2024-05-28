from django import forms
from librarian.models import BooksBorrowed
from .models import *

# Create Forms Here 
class BorrowBooksForm(forms.ModelForm):
    class Meta:
        model = BooksBorrowed
        fields = ('due_date', )
        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message', )