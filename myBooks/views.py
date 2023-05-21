from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .models import Author
from .serializers import AuthorSerializer, BookSerializer
from .pagination import DefaultPagination
from .filters import AuthorFilter


# Create your views here.
# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# def get_queryset(self):
#     return Author.objects.all()
#
# def get_serializer_class(self):
#     return AuthorSerializer


# Class based
# class ListOfAuthors(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         authors_serializer = AuthorSerializer(authors, many=True)
#         return Response(authors_serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Success", status=status.HTTP_201_CREATED)

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination


#
# class AuthorDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


def get_serializer_context(self):
    return {"request": self.request}


# def put(self, request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     author_serializer = AuthorSerializer(author, data=request.data)
#     author_serializer.is_valid(raise_exception=True)
#     author_serializer.save()
#     return Response("Detail updated successfully", status=status.HTTP_200_OK)
#
# def get(self, request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     author_serializer = AuthorSerializer(author)
#     return Response(author_serializer.data, status=status.HTTP_200_OK)
#
# def delete(self, request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     author.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
#


# def list_of_books(requests):
#     books = Book.objects.all()
#     return render(requests, 'myBooks/home.html', {'books': books})
#

# @api_view(['GET', 'POST'])
# def list_of_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         authors_serializer = AuthorSerializer(authors, many=True)
#         return Response(authors_serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         # the line below is where deserialization takes place Json back to object
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Success", status=status.HTTP_201_CREATED)
#     # return render(requests, 'myBooks/list_of_authors.html', {'authors': authors})
#     # return Response("OK")


@api_view()
def welcome(requests):
    return Response("Welcome Pal!")

# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         # author = Author.objects.get(pk=pk)
#         author_serializer = AuthorSerializer(author)
#         return Response(author_serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         author_serializer = AuthorSerializer(author, data=request.data)
#         author_serializer.is_valid(raise_exception=True)
#         author_serializer.save()
#         return Response("Detail updated successfully", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         if author.book_set.count() > 0:
#             return Response({"error": "Author associated with a book and cannot be deleted"},
#                             status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET', 'POST'])
# def list_of_books(request):
#     if request.method == 'GET':
#         all_books = Book.objects.all()
#         all_books_serializers = BookSerializer(all_books, many=True, context={'request': request})
#         return Response(all_books_serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("Success", status=status.HTTP_201_CREATED)
#
#
# @api_view(['PUT', 'GET', 'DELETE'])
# def book_details(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'PUT':
#         book_serializer = BookSerializer(book, data=request.data)
#         book_serializer.is_valid(raise_exception=True)
#         book_serializer.save()
#         return Response("Detail updated successfully", status=status.HTTP_200_OK)
#     elif request.method == 'GET':
#         book_serializer = BookSerializer(book, context={'request': request})
#         return Response(book_serializer.data, status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
