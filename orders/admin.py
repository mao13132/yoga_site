from django.contrib import admin

# Register your models here.
from .models import Orders


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('offer', 'name', 'phone', 'telegram', 'price', 'source', 'buy_chat', 'link',
                    'ip', 'date', 'comments')
    fields = ('offer', 'name', 'phone', 'telegram', 'price', 'comments', 'source', 'buy_chat', 'link')
    list_filter = ('date',)
    list_display_links = ('offer', 'name', 'phone', 'telegram', 'price', 'comments', 'source', 'ip', 'date', 'buy_chat',
                          'link')
    search_fields = ('offer', 'name', 'phone', 'telegram', 'comments', 'source', 'ip', 'date', 'buy_chat', 'link')


admin.site.register(Orders, OrdersAdmin)
