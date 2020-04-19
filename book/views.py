from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect

# Create your views here.
from book.models import CommentForm, Comment


@login_required(login_url='login')  # login durumuna göre fonksiyonun çalışıp çalışmaması butonu gizlemeseydik.
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')  # Get last url
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.book_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz Başarı ile Gönderilmiştir. Teşekkürler.")
            return HttpResponseRedirect(url)
    messages.warning(request, "Yorumunuz kaydedilemedi.")
    return HttpResponseRedirect(url)
