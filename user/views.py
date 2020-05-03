from django.shortcuts import render

# Create your views here.
from book.models import Category
from home.models import Setting, UserProfile


def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'settings': settings, "category": category, "profile": profile}
    return render(request, 'user_profile.html', context)
