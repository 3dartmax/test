from django import forms

class MyForm(forms.Form):
    name    = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'default'}))
    title   = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'default'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80 }))
