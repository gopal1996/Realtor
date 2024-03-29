from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25



admin.site.register(Realtor, RealtorAdmin)