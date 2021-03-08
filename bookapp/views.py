from django.shortcuts import render
from .models import Book, Category



def home(request):
    recommended_books = Book.objects.filter(recommended_books = True)
    fiction_books = Book.objects.filter(fiction_books = True)
    business_books = Book.objects.filter(business_books = True)
    return render(request, 'home.html', {
        'recommended_books': recommended_books,
        'fiction_books': fiction_books,
        'business_books': business_books,
    })