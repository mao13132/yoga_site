from django.contrib import admin

from django.contrib import messages

from .models import *

from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin


class MyAdminSite(AdminSite):

    def get_app_list(self, request, app_label=None):
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


class Page6TitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')


class Page6SessionAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'title3', 'title4')
    list_display_links = ('title1', 'title2', 'title3', 'title4')


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


class AbonimentsTitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('image',)


class AbonimentsCardsAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'price', 'id_chat')


class LeadPageAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'button')


class QuestsTitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')


class QuestsAdmin(admin.ModelAdmin):
    list_display = ('quest',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title1', 'telegram')


class LeadFormTitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')


class FreeFormTitleAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2')


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
admin.site.register(Page6Title, Page6TitleAdmin)
admin.site.register(Page6Session, Page6SessionAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(AbonimentsTitle, AbonimentsTitleAdmin)
admin.site.register(AbonimentsCards, AbonimentsCardsAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(LeadPage, LeadPageAdmin)
admin.site.register(QuestsTitle, QuestsTitleAdmin)
admin.site.register(Quests, QuestsAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(LeadFormTitle, LeadFormTitleAdmin)
admin.site.register(FreeFormTitle, FreeFormTitleAdmin)
