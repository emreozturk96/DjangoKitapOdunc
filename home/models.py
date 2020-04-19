from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea

from book.models import Book


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    company = models.CharField(blank=True, max_length=70)
    address = models.TextField(blank=True)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=70)
    smtpserver = models.CharField(blank=True, max_length=30)
    smtpemail = models.CharField(blank=True, max_length=70)
    smtppasswords = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=6)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=150)
    instagram = models.CharField(blank=True, max_length=150)
    twitter = models.CharField(blank=True, max_length=150)
    aboutus = RichTextUploadingField(blank=True)
    contactus = RichTextUploadingField(blank=True)
    haritaframe = RichTextUploadingField(blank=True)
    references = RichTextUploadingField (blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=40)
    email = models.CharField(blank=True, max_length=60)
    subject = models.CharField(blank=True, max_length=50)
    message = models.CharField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'name & surname'}),
            'email': TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Email Address'}),
            'subject': TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input-xlarge', 'placeholder': 'Your Message', 'rows': '5'}),
        }


class Slider(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = RichTextUploadingField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS, default='False')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

