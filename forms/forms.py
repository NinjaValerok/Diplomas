from django import forms

class MatrixSizesForm(forms.Form):
    number_rows = forms.IntegerField(min_value=1)
    number_column = forms.IntegerField(min_value=1)
    default_value = forms.IntegerField()

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

