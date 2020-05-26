from django.contrib import admin

# Register your models here.
from order.models import ShopCard, Order, OrderBook


class ShopCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'start_date', 'end_date')


class OrderProductline(admin.TabularInline):
    model = OrderBook
    readonly_fields = ('user', 'book')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'status')
    list_filter = ['status']
    readonly_fields = ('user',)
    inlines = [OrderProductline]


class OrderBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status')
    list_filter = ['user']


admin.site.register(ShopCard, ShopCardAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderBook, OrderBookAdmin)
