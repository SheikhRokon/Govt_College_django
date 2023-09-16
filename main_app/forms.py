from django import forms
from .models import Contact_form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_form 
        fields = "__all__"
        