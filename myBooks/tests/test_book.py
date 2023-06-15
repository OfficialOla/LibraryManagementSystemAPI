import pytest
from rest_framework.test import APIClient
from rest_framework import status

from myBooks.models import User


@pytest.mark.django_db
class TestBookEndPoint:

    def test_that_anonymous_user_cannot_get_book(self):
        client = APIClient()
        response = client.post('/library/books/', {"title": "Clinical Specialist_test"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_that_admin_user_can_get_book(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.get('/library/books/')
        assert response.status_code == status.HTTP_200_OK

    def test_that_admin_get_400_with_invalid_data(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/library/books/', {"title": "a", "genre": "C", "price": 428.32,
                                                   "isbn": "916846781-8", "author": 94})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_that_book_is_created_when_all_details_are_correct(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/library/books/', {"title": "Software Consultant",
                                                   "description": "A day in a life of a software engr",
                                                   "language": "Y",
                                                   "genre": "FIC",
                                                   "price": 707.24,
                                                   "isbn": "155893375-1", "author": 1})
        assert response.status_code == status.HTTP_201_CREATED
