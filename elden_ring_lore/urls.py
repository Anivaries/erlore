from django.contrib import admin
from django.conf import settings
from base.models import Lore, GroupModel
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'lores'
urlpatterns = []

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls),]

group_dict = {
    'queryset': GroupModel.objects.all(), 
    
}
lore_dict = {
    'queryset': Lore.objects.all(),
}

urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('sitemap.xml', sitemap, {
        'sitemaps': {
            'groups': GenericSitemap(group_dict, priority=0.6),
            'lore': GenericSitemap(lore_dict, priority=0.6),
            }, 
    }, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
