from django import forms
from .models import *

class GroupImage(forms.ModelForm):

    class Meta:
        model = GroupModel
        fields = ['group_name', 'group_image']
