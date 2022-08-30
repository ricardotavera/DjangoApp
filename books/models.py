from django.db import models
from author.models import Author
from category.models import Category


# Create your models here.
class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500, default=0)
    release_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now=True)
