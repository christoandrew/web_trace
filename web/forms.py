from django.db.models import TextField
from django.forms import forms, CharField


class ArticleForm(forms.Form):
    title = CharField(max_length=255)
    content = CharField(max_length=10000)
    description = CharField(max_length=255)
