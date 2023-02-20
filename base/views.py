from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Lore, LoreItem, GroupModel
from django.core.paginator import Paginator
from urllib import request


class GroupModelListView(ListView):
    model = GroupModel
    context_object_name = 'group_list'
    template_name: str = 'base/group.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group"] = GroupModel.objects.all()
        return context


class loreitemView(ListView):
    model = Lore
    context_object_name = 'lore_list'
    template_name = 'base/lore_list.html'
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return super().get_queryset().filter(belongs_to__group_name=GroupModel.objects.get(pk=pk))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['title'] = GroupModel.objects.filter(group_name=GroupModel.objects.get(pk=pk))
        return context  

class LoreItemListView(ListView):
    model = LoreItem
    context_object_name = 'loreitems'
    template_name = 'base/item.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return super().get_queryset().filter(item_type__name=Lore.objects.get(pk=pk))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context["naziv"] = Lore.objects.filter(name=Lore.objects.get(pk=pk))
        return context
