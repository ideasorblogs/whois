from django.contrib import admin
from .models import *
# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    list_display = ['keywords', 'ses_id', 'ip', 'created_on', 'count']

admin.site.register(SearchTerm,SearchAdmin)
