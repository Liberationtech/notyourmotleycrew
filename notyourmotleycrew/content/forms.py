from django.forms import ModelForm
from django import forms
from notyourmotleycrew.content.models import NYMCImage

class ImageForm(forms.Form):
    image = forms.FileField()
    #caption = forms.CharField(max_length=140,  label="A nice caption, no more then 140 characters")
    caption = forms.CharField(max_length=140,  
            widget=forms.TextInput(attrs={'placeholder': 'No more then 140 chars...'}))


class SignForm(forms.Form):
    text = forms.CharField(max_length=140,  
            widget=forms.TextInput(attrs={'placeholder': 'Your message goes here!'}))

