from django import forms
from .models import Menuitem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menuitem
        fields = ['item_title', 'item_description', 'item_image']