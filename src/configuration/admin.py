from django.contrib import admin

from src.configuration.models import Seo, Social, Config
from modeltranslation.translator import TranslationOptions, translator

admin.site.site_header = "SAFT панель управления"
admin.site.site_title = "SAFT панель управления"
admin.site.index_title = 'Добро пожаловать!'


class ConfigTranslationOption(TranslationOptions):
    fields = ('address',)
    required_languages = ('az',)


translator.register(Config, ConfigTranslationOption)


class SeoTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'keywords')
    required_languages = ('az',)


translator.register(Seo, SeoTranslationOption)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name',)
