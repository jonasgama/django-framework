from django.contrib import admin

from .models import Contact, Category


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
