from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'lores'
urlpatterns = []

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls),]

urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
