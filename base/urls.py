from django.urls import path
from .views import LoreitemView, LoreItemListView, GroupModelListView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'lores'
urlpatterns = [
    path('', GroupModelListView.as_view(), name="group"),
    path('lore/<int:pk>/', LoreitemView.as_view(), name="lore_list"),
    path('item/<int:pk>/', LoreItemListView.as_view(), name='loreitems'),
    # path('search/', SearchResults.as_view(), name='search_result'), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)