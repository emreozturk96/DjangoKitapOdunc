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


class Order(models.Model):
    STATUS = (
        ('Yeni', 'Yeni'),
        ('Onaylandi', 'Onaylandi'),
        ('TeslimEdildi', 'TeslimEdildi'),
        ('GeriAlindi', 'GeriAlindi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    adminnote = models.TextField(blank=True, max_length=200)
    status = models.CharField(choices=STATUS, default='Yeni', max_length=20)
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name 


class OrderBook(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='New', max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title
