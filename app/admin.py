from django.contrib import admin
from .models import *
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ['Type']
admin.site.register(Type, TypeAdmin)

class HolidaysAdmin(admin.ModelAdmin):
    list_display = ['Notes', 'type']
admin.site.register(Holidays, HolidaysAdmin)
