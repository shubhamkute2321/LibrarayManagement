from django import forms
from django import forms

from apps.models import Book

class Bookfrom(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"