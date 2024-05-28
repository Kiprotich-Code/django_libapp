from django.db import models
from users.models import CustomUser
from django.utils import timezone

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    ISBN = models.CharField(max_length=20, blank=True)
    author = models.CharField(max_length=200, blank=True)
    year_published = models.IntegerField()
    copies = models.IntegerField()

    def __str__(self):
        return f'{self.title} by {self.author}'
    

class BooksBorrowed(models.Model):
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('returned', 'Returned'),
    ]

    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='books')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')