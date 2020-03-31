from django.contrib import admin

from book.models import Category, Book, Images

class BookImagesInline(admin.TabularInline):
    model = Images
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['category']
    inlines = [BookImagesInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'book', 'image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Images, ImagesAdmin)

