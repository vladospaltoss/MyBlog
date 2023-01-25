from django import forms

class UserForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    body = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput)