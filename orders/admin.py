from django.contrib import admin

# Register your models here.
from .models import Orders


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('offer', 'name', 'phone', 'telegram', 'price', 'comments', 'source', 'buy_chat', 'ip', 'date')
    fields = ('offer', 'name', 'phone', 'telegram', 'comments', 'source', 'price', 'buy_chat')
    list_filter = ('date',)
    list_display_links = ('offer', 'name', 'phone', 'telegram', 'price', 'comments', 'source', 'ip', 'date', 'buy_chat')


admin.site.register(Orders, OrdersAdmin)
