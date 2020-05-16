from django.contrib import admin


# Register your models here.
from order.models import ShopCard


class ShopCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'day')


admin.site.register(ShopCard, ShopCardAdmin)
