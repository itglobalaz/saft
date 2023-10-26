from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from src.main.models import About, AboutLabel, Slider, WhyUs, WhyUsBlock, Partners


class AboutLabelInline(TranslationTabularInline):
    model = AboutLabel
    extra = 1

    verbose_name = "Punkt"
    verbose_name_plural = "Punktlar"


class AboutTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('title',)
    required_languages = ('az',)
    summernote_fields = ('description',)
    inlines = [AboutLabelInline]

    fieldsets = (
        ('Məlumat', {
            'fields': ('photo', 'title', 'description')
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(About, AboutTranslationOptions)


class WhyusInline(TranslationTabularInline):
    model = WhyUsBlock
    extra = 1

    verbose_name = "Blok"
    verbose_name_plural = "Misal: fa-cubes | https://fontawesome.com/v4/icons/"

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class WhyUsTranslationOptions(TabbedTranslationAdmin):
    list_display = ('title',)
    required_languages = ('az',)
    inlines = [WhyusInline]
    fieldsets = (
        ('Məlumat', {
            'fields': ('image', 'title',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(WhyUs, WhyUsTranslationOptions)


class SliderTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'image', 'get_image',)
    list_editable = ('image',)
    summernote_fields = ('description',)
    prepopulated_fields = {'slug': ('subtitle',)}

    ordering = ['id']


admin.site.register(Slider, SliderTranslationOptions)


class PartnersTranslationOptions(TabbedTranslationAdmin, SummernoteModelAdmin):
    list_display = ('name',)
    summernote_fields = ('description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Partners, PartnersTranslationOptions)
