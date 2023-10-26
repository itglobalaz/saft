from django.template import Library

from src.configuration.models import Config, Seo, Social
from src.main.models import Partners

register = Library()


@register.simple_tag()
def get_config():
    return Config.objects.get()


@register.simple_tag()
def get_seo():
    return Seo.objects.get()


@register.simple_tag()
def get_social():
    return Social.objects.order_by('-id')


@register.simple_tag()
def get_partners():
    return Partners.objects.order_by('name')[:15]
