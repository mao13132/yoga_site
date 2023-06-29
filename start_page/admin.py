from django.contrib import admin

from django.contrib import messages

from .models import Settings, ButtonsHead, Page2Title


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


class ButtonsHeadAdmin(admin.ModelAdmin):
    list_display = ('button1', 'button2', 'button3', 'button4', 'button5', 'button6')


class Page2TitleAdmin(admin.ModelAdmin):
    list_display = ('h1', 'disc1', 'disc1')


admin.site.register(Settings, SettingsAdmin)
admin.site.register(ButtonsHead, ButtonsHeadAdmin)
admin.site.register(Page2Title, Page2TitleAdmin)
