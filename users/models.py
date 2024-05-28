from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('non_member', 'Non_Member'),
    ]
    
    username = None
    email = models.EmailField(unique=True)
    full_names = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Student')
    admission_no = models.CharField(max_length=50, blank=True)
    staff_id = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_names', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.full_names