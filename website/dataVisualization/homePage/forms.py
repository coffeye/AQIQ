from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')