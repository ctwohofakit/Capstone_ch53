from django import forms

class ContactForm(forms.Form):
    firstname=forms.CharField(max_length=200)
    lastname=forms.CharField(max_length=200)
    email=forms.CharField(max_length=200, widget=forms.TextInput(attrs={"type":"email"}))
    subject=forms.CharField(max_length=200)
    message=forms.CharField(widget=forms.Textarea())