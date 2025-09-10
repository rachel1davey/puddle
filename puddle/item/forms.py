from django import forms
from .models import Item


MASTER_CLASS = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image')
   
        widgets = {
            'category': forms.Select(attrs={
                'class': MASTER_CLASS
                }),
            'name': forms.TextInput(attrs={
                'class': MASTER_CLASS
                }),
            'description': forms.Textarea(attrs={
                'class': MASTER_CLASS
                }),
            'price': forms.TextInput(attrs={
                'class': MASTER_CLASS
                }),
            'image': forms.FileInput(attrs={
                'class': MASTER_CLASS
                }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'isSold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': MASTER_CLASS
                }),
            'description': forms.Textarea(attrs={
                'class': MASTER_CLASS
                }),
            'price': forms.TextInput(attrs={
                'class': MASTER_CLASS
                }),
            'image': forms.FileInput(attrs={
                'class': MASTER_CLASS
                }),
            'isSold': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-blue-600'
                }),
        }
