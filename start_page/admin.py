from django.contrib import admin

from django.contrib import messages

from .models import Settings, ButtonsHead, Page2Title, Page2Slider, Advantages, Page4Title, Page4Cards, \
    Page5Title, Page5Cards

from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin


class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        # for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list


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


class Page2SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')


class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class Page4TitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')


class Page4CardsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class Page5TitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'desc')


class Page5CardsAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'desc')


admin.site = MyAdminSite()

admin.site.register(Settings, SettingsAdmin)
admin.site.register(ButtonsHead, ButtonsHeadAdmin)
admin.site.register(Page2Title, Page2TitleAdmin)
admin.site.register(Page2Slider, Page2SliderAdmin)
admin.site.register(Advantages, AdvantagesAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Page4Title, Page4TitleAdmin)
admin.site.register(Page4Cards, Page4CardsAdmin)
admin.site.register(Page5Title, Page5TitleAdmin)
admin.site.register(Page5Cards, Page5CardsAdmin)
