from django.forms import DateTimeInput, ModelForm, Textarea, TextInput

from .models import News


class ArticlesForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"

        widgets = {
            "title": TextInput(attrs={"class": "form-control", "placeholder": "TITLE"}),
            "anons": TextInput(attrs={"class": "form-control", "placeholder": "DESCRIPTION"}),
            "date": DateTimeInput(attrs={"class": "form-control", "placeholder": "DATE"}),
            "full_text": Textarea(attrs={"class": "form-control", "placeholder": "TEXT"}),
        }
