from django import forms

class MyFileuploadForm(forms.Form):
    file_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    files=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))