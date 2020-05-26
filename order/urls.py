
from django.urls import path

from order import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtocard/<int:id>', views.addtocard, name='addtocard'),
    path('deletefromcard/<int:id>', views.deletefromcard, name='deletefromcard'),
    path('updatedatefromcard/<int:id>', views.updatedates, name='updatedates'),
    path('orderbook/', views.orderbook, name='orderbook'),
]