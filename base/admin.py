from django.contrib import admin
from .models import Lore, LoreItem, GroupModel

admin.site.register(GroupModel)

@admin.register(Lore)
class LoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'belongs_to')

@admin.register(LoreItem)
class LoreItemAdmin(admin.ModelAdmin):
    list_display = ['item_title', 'show_item_type', 'item_description']
    search_fields = ['item_type__name']

    def show_item_type(self, obj):
        return "\n".join([a.name for a in obj.item_type.all()])
