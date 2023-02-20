from django.urls import path
from .views import loreitemView, LoreItemListView, GroupModelListView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'lores'
urlpatterns = [
    path('', GroupModelListView.as_view(), name="group"),
    path('lore/<int:pk>/', loreitemView.as_view(), name="lore_list"),
    path('item/<int:pk>/', LoreItemListView.as_view(), name='loreitems'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)