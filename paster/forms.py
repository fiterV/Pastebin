from django import forms

class PasteForm(forms.Form):
    text = forms.TextField(widget=forms.Textarea)
    title = forms.CharField(max_length=200, widget=forms.CharField)

