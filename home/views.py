from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    settings = Setting.objects.get(pk=1)
    context = {'settings': settings}
    return render(request, 'index.html', context)

    # return HttpResponse(" Deneme Sayfası %s." % text)