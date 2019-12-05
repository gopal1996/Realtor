from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id',)
    list_filter = ('realtor',)
    list_editable = ('title','is_published')
    search_fields = ('title',)
    list_per_page = 25



admin.site.register(Listing, ListingAdmin)
