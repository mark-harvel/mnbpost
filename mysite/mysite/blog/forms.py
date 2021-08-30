from django.forms import fields
from .models import Comment, Signup
from django import forms

class CommmentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
