from .models import Category
from django.forms.models import ModelForm

class Add_category(ModelForm):
    class Meta:
        models = Category
        fields = "__all__"