from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('categories',max_length=200)
    slug = models.SlugField(max_length=200)
        
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_lenth=100)
    summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    pdf = models.FileField(upload_to='pdf')
    recommended_books = models.BooleanField(default=False)
    fiction_books = models.BooleanField(default=False)
    business_books = models.BooleanField(default=False)