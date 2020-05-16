from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from order.models import ShopCardForm, ShopCard


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
        form = ShopCardForm(request.POST)
        if form.is_valid():
            if control == 1:
                messages.warning(request, "Kitap Sepete Ekli.")
            else:
                data = ShopCard()
                data.user_id = current_user.id
                data.book_id = id
                data.day = form.cleaned_data['day']
                data.save()
                messages.success(request, "Başarıyla sepete eklenmiştir.")
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            messages.warning(request, "Kitap Sepete Ekli.")
        else:
            data = ShopCard()
            data.user_id = current_user.id
            data.book_id = id
            data.day = 7
            data.save()
            messages.success(request, "Başarıyla sepete eklenmiştir.")
    return HttpResponseRedirect(url)

    messages.warning(request, "Sepete Eklerken hata.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def shopcard(request):
    current_user = request.user
    shopcardd = ShopCard.objects.filter(user_id=current_user.id)
    context = {'shopcardd': shopcardd}
    return render(request, 'shopcard.html', context)


@login_required(login_url='/login')
def deletefromcard(request, id):
    ShopCard.objects.filter(id=id).delete()
    messages.success(request, "Kitap Sepetten Silindi.")
    return HttpResponseRedirect("/shopcard")
