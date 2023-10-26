from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Partners, Slider


class PartnersSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Partners.objects.all()

    def location(self, obj):
        return reverse('partner_detail', args=[obj.slug])


class StaticPages(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class SlidersSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Slider.objects.all()

    def location(self, obj):
        return reverse('slider_detail', args=[obj.slug])
