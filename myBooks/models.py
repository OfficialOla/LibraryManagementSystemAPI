from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# Always define your User before the database,
# do this below and go to your settings AUTH_USER_MODEL and write the name of the appName.user
# even if you're not sure of the fields, just do this first class User(AbstractUser): pass
# You can change the behaviour of the fields in abstract user

class User(AbstractUser):
    email = models.EmailField(unique=True)

    # def __str__(self):
    #     return f" Author's name is, {self.first_name} {self.last_name}"


# you can add any other fields here

class Author(models.Model):
    # Blank = input field
    # null = database
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f" Author's name is, {self.first_name} {self.last_name}"


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ('Y', 'YORUBA'),
        ('H', 'HAUSA'),
        ('I', 'IGBO'),
        ('E', 'ENGLISH')
    ]
    GENRE_CHOICES = [
        ('FIC', 'FICTION'),
        ('POL', 'POLITICS'),
        ('FIN', 'FINANCE'),
        ('ROM', 'ROMANCE')
    ]
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)

    def __str__(self):
        return f" {self.author} {self.title} {self.price} "


# class Genre(models.Model):
#     name = models.CharField(max_length=55)
#
#     def __str__(self):
#         return f" {self.name}"


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"   {self.status} {self.book} "
