from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import datetime
# Create your views here.
from django.utils.crypto import get_random_string

from book.models import Book
from home.models import Setting
from order.forms import DateRangeForm
from order.models import ShopCard, Order, OrderBook


def index(request):
    return HttpResponse("Order App")


@login_required(login_url='/login')
def addtocard(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkbook = ShopCard.objects.filter(book_id=id)
    if checkbook:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        if control == 1:
            messages.warning(request, "Kitap Sepete Ekli.")
        else:
            data = ShopCard()
            data.user_id = current_user.id
            data.book_id = id
            data.start_date = request.POST['start_date']
            data.end_date = request.POST['end_date']
            data.save()
            request.session['card_items'] = ShopCard.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Başarıyla sepete eklenmiştir.")
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            messages.warning(request, "Kitap Sepete Ekli.")
        else:
            data = ShopCard()
            data.user_id = current_user.id
            data.book_id = id
            data.start_date = datetime.datetime.now()
            data.end_date = datetime.datetime.now() + datetime.timedelta(days=7)
            data.save()
            request.session['card_items'] = ShopCard.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Başarıyla sepete eklenmiştir.")
        return HttpResponseRedirect(url)

    messages.warning(request, "Sepete Eklerken hata.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def shopcard(request):
    current_user = request.user
    settings = Setting.objects.get(pk=1)
    shopcardd = ShopCard.objects.filter(user_id=current_user.id)
    request.session['card_items'] = ShopCard.objects.filter(user_id=current_user.id).count()
    start = datetime.datetime.now()
    end = datetime.datetime.now() + datetime.timedelta(days=7)
    context = {'shopcardd': shopcardd, 'settings': settings, 'start': start, 'end': end}
    return render(request, 'shopcard.html', context)


@login_required(login_url='/login')
def deletefromcard(request, id):
    ShopCard.objects.filter(id=id).delete()
    current_user = request.user
    request.session['card_items'] = ShopCard.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Kitap Sepetten Silindi.")
    return HttpResponseRedirect("/shopcard")


@login_required(login_url='/login')
def updatedates(request, id):
    current_user = request.user
    data = ShopCard.objects.get(id=id)
    data.start_date = request.POST['start_date']
    data.end_date = request.POST['end_date']
    data.save()
    request.session['card_items'] = ShopCard.objects.filter(user_id=current_user.id).count()
    messages.success(request, "Tarih Güncellendi.")
    return HttpResponseRedirect("/shopcard")


@login_required(login_url='/login')
def orderbook(request):
    settings = Setting.objects.get(pk=1)
    current_user = request.user
    data = Order()
    data.user_id = current_user.id
    data.ip = request.META.get('REMOTE_ADDR')
    ordercode = get_random_string(5).upper()
    data.code = ordercode
    data.save()

    schopcard = ShopCard.objects.filter(user_id=current_user.id)
    for rs in schopcard:
        detail = OrderBook()
        detail.order_id = data.id
        detail.book_id = rs.book_id
        detail.user_id = current_user.id
        detail.start_date = rs.start_date
        detail.end_date = rs.end_date
        detail.end_date = rs.end_date
        detail.save()

        book = Book.objects.get(id=rs.book_id)
        book.amount -= 1
        book.save()

    ShopCard.objects.filter(user_id=current_user.id).delete()
    request.session['card_items'] = 0
    messages.success(request, "Rezervasyon tamamlandi.")
    return render(request, 'order_completed.html', {'ordercode': ordercode, 'settings': settings, 'user': current_user})
