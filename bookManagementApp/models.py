from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title() # admin에서 book list를 출력할 때 default 객체 번호가 아닌 객체의 title을 출력
        
# Create your models here.
