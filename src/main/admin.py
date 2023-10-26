from django.contrib import admin
from modeltranslation.translator import translator, TranslationOptions
from src.main.models import AboutLabel, About, Slider, WhyUs, WhyUsBlock, Partners
from django_summernote.models import Attachment

admin.site.unregister(Attachment)


class AboutTranslationOption(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = ('az',)


translator.register(About, AboutTranslationOption)


class AboutLabelTranslationOption(TranslationOptions):
    fields = ('title',)
    required_languages = ('az',)


translator.register(AboutLabel, AboutLabelTranslationOption)


class SliderTranslationOption(TranslationOptions):
    fields = ('title', 'subtitle', 'description',)


translator.register(Slider, SliderTranslationOption)


class WhyUsTranslationOption(TranslationOptions):
    fields = ('title',)
    required_languages = ('az',)


translator.register(WhyUs, WhyUsTranslationOption)


class WhyUsBlockTranslationOption(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('az',)


translator.register(WhyUsBlock, WhyUsBlockTranslationOption)


class PartnersTranslationOption(TranslationOptions):
    fields = ('description',)


translator.register(Partners, PartnersTranslationOption)
