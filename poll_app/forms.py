from django.forms import ModelForm
from .models import Poll

class NewPollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'one', 'two', 'three']
