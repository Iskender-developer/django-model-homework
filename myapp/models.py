from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    name = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    info = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
    is_available = models.BooleanField(default=True)
    publishers = models.ManyToManyField(Publisher)
    number_books = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Staff(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    staff_email = models.EmailField(max_length=255)
    is_works_weekend = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Borrow(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    opinion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CardId(models.Model):
    id_number = models.CharField(max_length=16, unique=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



