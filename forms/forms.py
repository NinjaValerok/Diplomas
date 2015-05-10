from django import forms

class MatrixSizesForm(forms.Form):
    number_rows = forms.IntegerField(min_value=1)
    number_column = forms.IntegerField(min_value=1)
    number_PCA = forms.IntegerField(min_value=1)
    default_value = forms.IntegerField()
