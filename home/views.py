from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from book.models import Category, Book
from home.models import Setting, ContactForm, ContactFormMessage, Slider


def index(request):
    settings = Setting.objects.get(pk=1)
    sliderdata = Slider.objects.all()[1:4]
    sliderfirst = Slider.objects.first()
    category = Category.objects.all()
    books = Book.objects.all().order_by('?')[:9]
    context = {'settings': settings, 'sliderdata': sliderdata, 'sliderfirst': sliderfirst, "category": category, "books": books}
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
    context = {'books': books, "category": category, "categorydata": categorydata}
    return render(request, 'books.html', context)
