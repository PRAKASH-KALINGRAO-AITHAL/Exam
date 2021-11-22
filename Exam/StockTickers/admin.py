from django.contrib import admin
from .models import Student

admin.site.register(Student)
class StockTicksAdmin(admin.ModelAdmin):
    list_display=("RegNum","Name")
    