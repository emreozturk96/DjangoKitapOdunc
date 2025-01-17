import datetime
import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from book.models import Category, Book, Images, Comment
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, Slider, FAQ
from order.models import ShopCard


def index(request):
    settings = Setting.objects.get(pk=1)
    sliderfirst = Slider.objects.first()
    category = Category.objects.all()
    books = Book.objects.all().order_by('?')[:9]
    bookfirst = Book.objects.first()
    bookslider = Book.objects.all().order_by('id')[1:4]
    current_user = request.user
    request.session['card_items'] = ShopCard.objects.filter(user_id=current_user.id).count()
    context = {'settings': settings, 'bookfirst': bookfirst, 'sliderfirst': sliderfirst, "category": category,
               "books": books, "bookslider": bookslider}
    return render(request, 'index.html', context)
    # return HttpResponse(" Deneme Sayfası %s." % text)


def hakkimizda(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Mesajınız Başarı İle Gönderilmiştir. Teşekkürler.")
            return HttpResponseRedirect('/iletisim')

    settings = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'settings': settings, 'form': form}
    return render(request, 'iletisim.html', context)


def category_books(request, id, slug):
    books = Book.objects.filter(category_id=id)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    bookfirst = Book.objects.first()
    context = {'books': books, "category": category, "categorydata": categorydata, "bookfirst": bookfirst}
    return render(request, 'books.html', context)


def book_detail(request, id, slug):
    category = Category.objects.all()
    bookfirst = Book.objects.first()
    book = Book.objects.get(pk=id)
    images = Images.objects.filter(book_id=id)
    comments = Comment.objects.filter(book_id=id, status='True')
    start = datetime.datetime.now()
    context = {"category": category, "book": book, "images": images, "comments": comments, "start": start,
               "bookfirst": bookfirst}
    return render(request, 'book_detail.html', context)


def book_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            context = {"category": category, "books": books}
            return render(request, 'book_search.html', context)

    return HttpResponseRedirect('/')


def book_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        books = Book.objects.filter(title__icontains=q)
        results = []
        for rs in books:
            book_json = {}
            book_json = rs.title
            results.append(book_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Kullanıcı Adı veya Şifre yanliş.")
            return HttpResponseRedirect('/login')

    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'settings': settings, "category": category, }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Hata Oluştu")
            return HttpResponseRedirect('/signup')

    form = SignUpForm()
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'settings': settings, "category": category, "form": form}
    return render(request, 'signup.html', context)


def faq(request):
    settings = Setting.objects.get(pk=1)
    faqs = FAQ.objects.filter(status='True').order_by('ordernumber')
    context = {'settings': settings, 'faqs': faqs}
    return render(request, 'faq.html', context)
