import decimal

from _decimal import Decimal
from rest_framework import serializers

from myBooks.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # date_of_birth = serializers.DateField()


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'price', 'genre', 'book_number', 'discount_price', 'price', 'author']

    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author-detail'
    # )
    book_number = serializers.CharField(max_length=13, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    # the price is referencing the Book type/class
    def calculate(self, book: Book):
        return book.price * Decimal(0.1)

    # title = serializers.CharField(max_length=255)
    # book_author = serializers.CharField(max_length=255, source='author')
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # genre = serializers.CharField(max_length=10, )
    # book_number = serializers.CharField(max_length=13, source='isbn')
