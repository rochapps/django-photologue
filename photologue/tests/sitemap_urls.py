from django.conf.urls import url, include

from photologue.sitemaps import PhotologueSitemap

# Note: this urls definition file is used only for sitemap tests at the moment.
# Maybe it should be extended at a later date?

urlpatterns = [
    url(r'^photologue/', include('photologue.urls')),
]

sitemaps = {'photologue': PhotologueSitemap}

urlpatterns += [
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
]
