from django import forms
from .models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']