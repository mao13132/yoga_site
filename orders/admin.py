from django.contrib import admin

# Register your models here.
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'telegram', 'price', 'comments', 'source', 'ip', 'date')
    fields = ('name', 'phone', 'telegram', 'comments', 'source', 'price')
    list_filter = ('date',)
    list_display_links = ('name', 'phone', 'telegram', 'price', 'comments', 'source', 'ip', 'date')


admin.site.register(Orders, OrdersAdmin)
