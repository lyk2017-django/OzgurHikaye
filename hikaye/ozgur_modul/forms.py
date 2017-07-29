from django import forms
from ozgur_modul.models import Storys, Contributions
from django.forms import HiddenInput

class StoryNewForm(forms.ModelForm):
    """Yeni hikaye oluşturma formu"""
    class Meta:
        model = Storys
        exclude = ["id"]
        labels = {
            "story_title": "Hikayenizin Başlığı"
        }

class ContribituonsNewForm(forms.ModelForm):
    """Hikaye için katkı ekleme formu"""
    class Meta:
        model = Contributions
        exclude = ["id"]
        widgets = {
            "story": HiddenInput()
        }
        labels = {
            "contribution_text": "" # Ekranda bu sahanın etiketi görünmesin...
        }


#x=ContribituonsNewForm(request.POST)
#x.is_valid()
#x.save()