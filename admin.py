from django.contrib import admin
from .models import Start
# Register your models here.

class StartAdmin(admin.ModelAdmin):
    list_display = ("class_name","prof_name","comment")

admin.site.register(Start, StartAdmin)
