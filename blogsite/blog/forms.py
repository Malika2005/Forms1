from django import forms
from .models import Post

# class FoodForm(forms.Form):
#     title = forms.CharField(required=False, label='Food', initial='Cookie', help_text='LOOL')
#     price = forms.IntegerField(required=False, label='Cost')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'