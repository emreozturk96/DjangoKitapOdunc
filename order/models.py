from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput

from book.models import Book


class ShopCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    day = models.IntegerField()

    def __str__(self):
        return self.book.title


class ShopCardForm(ModelForm):
    class Meta:
        model = ShopCard
        fields = ['day']
