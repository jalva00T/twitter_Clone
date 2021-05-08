from django.forms import ModelForm      
from .models import Tweet

class PhotoForm(ModelForm):
  class Meta:
      model = Tweet
      