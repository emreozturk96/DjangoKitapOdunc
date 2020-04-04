from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, Slider


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(Setting)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(Slider, SliderAdmin)
