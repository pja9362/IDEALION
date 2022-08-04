from django import forms
from .models import contents
from  contents.models import categoryList

class ContentsForm(forms.ModelForm):
    class Meta:
        model = contents
        fields = ['title', 'detail', 'image']

        
class categoryForm(forms.ModelForm):
    class Meta:
        model = categoryList
        fields = ['name','share', 'icon']