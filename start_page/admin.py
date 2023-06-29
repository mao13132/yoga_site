from django.contrib import admin

from django.contrib import messages

from .models import Settings
# Register your models here.

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'h1_1', 'h1_2', 'button1', 'button2')
    list_display_links = ('title', 'description')
    search_fields = ('title',)

    # def save_model(self, request, obj, form, change):
    #
    #
    #
    #
    #     count = Settings.objects.count()
    #
    #
    #     if count >= 1:
    #         messages.add_message(request, messages.ERROR, 'Нельзя добавить новые настройки. ИЗМЕНЯЙТЕ старые')
    #     else:
    #         super(SettingsAdmin, self).save_model(request, obj, form, change)


admin.site.register(Settings, SettingsAdmin)

