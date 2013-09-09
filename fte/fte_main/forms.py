from django import forms

class FTEMainForm(forms.Form):
    custom_label = forms.CharField(max_length=30, required=True)
    infile = forms.FileField()
