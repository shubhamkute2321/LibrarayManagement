from django.db import models
import uuid
# Create your models here.
class Admin(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username

class Book(models.Model):
    book_name=models.CharField(max_length=50, blank=True, default='null', null=True)
    book_author=models.CharField(max_length=50, blank=True, default='null', null=True)
    book_publisher=models.CharField(max_length=50, blank=True, default='null', null=True)
    class Meta:
        verbose_name_plural = 'Book'   
    def __str__(self):
        return str(self.book_id)
