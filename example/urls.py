from django.urls import path, include
from rest_framework import routers
from .views import HelloAPI, BooksAPI, BookAPI, BookViewSet 

router = routers.SimpleRouter()
router.register('books',BookViewSet)

urlpatterns = router.urls

"""urlpatterns = [
    path("hello/",HelloAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>", BookAPI.as_view()),
]"""