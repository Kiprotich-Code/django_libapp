from django.contrib import admin
from .models import Books, BooksBorrowed

# Register your models here.
admin.site.register(Books)
admin.site.register(BooksBorrowed)