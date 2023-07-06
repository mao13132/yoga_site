from django.contrib import admin

from .models import Users, Links


# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_tg', 'login', 'email', 'phone', 'join_date', 'last_time', 'rang',
                    'license', 'start_license', 'ower_license', 'buy_chat', 'demo')
    fields = ('id_tg', 'name', 'full_name', 'login', 'email', 'phone', 'other', 'rang', 'license', 'ower_license',
              'buy_chat', 'demo')
    list_filter = ('join_date',)
    list_display_links = ('id_tg', 'login', 'email', 'phone', 'join_date', 'last_time',
                          'rang', 'license', 'start_license', 'ower_license', 'buy_chat', 'demo')
    search_fields = ('id_tg', 'login', 'license', 'start_license', 'ower_license')


class LinksAdmin(admin.ModelAdmin):
    list_display = ('buy_chat', 'id_tg', 'link', 'payment_link', 'push', 'date_connect', 'activ', 'kick', 'free', 'source',
                    'ower_license', 'start_license')

    fields = ('link', 'id_tg', 'buy_chat', 'start_license', 'ower_license', 'activ', 'kick', 'free', 'source',
              'payment_link', 'push')

    list_display_links = ('link', 'payment_link', 'id_tg', 'buy_chat', 'date_connect', 'start_license', 'ower_license',
                          'activ', 'kick', 'free', 'push'
                          , 'source')
    search_fields = ('link', 'id_tg', 'buy_chat', 'date_connect', 'start_license', 'ower_license', 'activ', 'kick',
                     'free', 'source', 'push')


admin.site.register(Users, UsersAdmin)

admin.site.register(Links, LinksAdmin)
