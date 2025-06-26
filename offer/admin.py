from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title','percentage','is_active']
    list_filter = ['is_active']
    search_fields = ['title']
    


      