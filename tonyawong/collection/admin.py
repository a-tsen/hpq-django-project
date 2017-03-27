from django.contrib import admin

from .models import Item

# Username: testing
# Password: The_Real_Thing


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_type')  # appears from Item model change page
    list_filter = ['item_type']  # can filter by type of item
    search_fields = ['item_name']  # can search by question name


admin.site.register(Item, ItemAdmin)
