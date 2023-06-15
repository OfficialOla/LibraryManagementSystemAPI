from django.contrib import admin
from .models import Author, User
from .models import Book
from .models import BookInstance
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['email']
    list_per_page = 10


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'author']
    list_filter = ['price']
    list_per_page = 10


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status']
    list_per_page = 10


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
    pass
