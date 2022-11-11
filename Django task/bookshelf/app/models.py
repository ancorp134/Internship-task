import email
from django.db import models
import uuid
from isbn_field import ISBNField

class BookShelf(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    isbn = ISBNField()
    pulication=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    

    def __str__(self):
        return self.name + self.author