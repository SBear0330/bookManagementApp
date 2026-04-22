from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
        
# Create your models here.
