from django import forms
from .models import Item

class ItemForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Item.objects.all(), label='Select Item')