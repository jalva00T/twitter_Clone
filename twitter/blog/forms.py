from django import forms      
from .models import Tweet

class PhotoForm(forms.ModelForm):
  class Meta:
      model = Tweet
      fields = '__all__' 