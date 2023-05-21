from . import views
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = router.urls
# print(router.urls)
#
# urlpatterns = [
#     # the name in the path below is an alias which can be used to call a url
#     path('', include(router.urls)),
#     # path('book/<int:pk>/', views.BookDetailView.as_view(), name='home'),
#     # path('authors/', views.AuthorList.as_view()),
#     # path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
#     # path('list_authors/', views.list_of_authors),
#     # path('books/', views.BookList.as_view())
# ]
