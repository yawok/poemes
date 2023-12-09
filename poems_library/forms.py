from django.forms import ModelForm
from . import models

class PoemForm(ModelForm):
    class Meta:
        model = models.Poem
        fields = ["title", "text"]
        