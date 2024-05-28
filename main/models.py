from django.db import models
from librarian.models import CustomUser

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.email}'
    

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'Feedback from {self.user}'