from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from book.models import Category
from home.models import Setting, UserProfile
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'settings': settings, "category": category, "profile": profile}
    return render(request, 'user_profile.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('/user')

    else:
        settings = Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'settings': settings, "user_form": user_form, "profile_form": profile_form}
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sifre Başarıyla değiştirildi.')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        settings = Setting.objects.get(pk=1)
        form = PasswordChangeForm(request.user)
        context = {'settings': settings, "form": form}
        return render(request, 'change_password.html', context)
