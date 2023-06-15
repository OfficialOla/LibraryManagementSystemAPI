from django_filters import FilterSet

from .models import Author, Book


# Class Meta is used for a nested class. when you
# want to show more details about a model or endpoint
class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            'first_name': ['exact']
        }


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'price': ['gt', 'lt']
        }
