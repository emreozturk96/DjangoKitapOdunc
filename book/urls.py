
from django.urls import path

from book import views

urlpatterns = [
    path('addcomment/<int:id>/', views.addcomment, name='addcomment'),
]