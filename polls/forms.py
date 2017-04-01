from django.forms import ModelForm

from polls.models import Thing

class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description', 'ingredients')