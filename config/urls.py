from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from src.main.sitemaps import *
sitemaps = {
    'partners': PartnersSitemap(),
    'home': StaticPages(),
    'sliders': SlidersSitemap(),
}

urlpatterns = i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('src.main.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  # new

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
