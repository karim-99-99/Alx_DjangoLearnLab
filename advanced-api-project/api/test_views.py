from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        
        self.user = User.obbjects.create_user(username='testuser', password='testpass')
        self.user2 = User.objects.create_user(username='otheruser', password='otherpass')


        self.author = Author.objects.create(name='Author 1')
        self.book = Book.objects.create(
            title='Book 1',
            author=self.author,
            publication_year=2020,
            owner=self.user
        )

        