from django.contrib import admin

from .models import Users


# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id_tg', 'name', 'full_name', 'login', 'email', 'phone', 'join_date', 'last_time', 'rang',
                    'license', 'start_license', 'ower_license', 'buy_chat', 'demo')
    fields = ('id_tg', 'name', 'full_name', 'login', 'email', 'phone', 'other', 'rang', 'license', 'ower_license',
              'buy_chat', 'demo')
    list_filter = ('join_date',)
    list_display_links = ('id_tg', 'name', 'full_name', 'login', 'email', 'phone', 'join_date', 'last_time',
                          'rang', 'license', 'start_license', 'ower_license', 'buy_chat', 'demo')


admin.site.register(Users, UsersAdmin)
