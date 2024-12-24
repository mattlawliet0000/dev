from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=100)
    contact_email = forms.EmailField()
    contact_message = forms.CharField(widget=forms.Textarea)
