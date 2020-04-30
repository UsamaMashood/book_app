import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model):

    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to = 'covers/', default=None)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books_detail', args = [str(self.pk)])
    


class Review(models.Model):
    comment = models.CharField(max_length=100)
    book = models.ForeignKey(
        Book,
        on_delete = models.CASCADE,
        related_name= 'reviews'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.comment
    