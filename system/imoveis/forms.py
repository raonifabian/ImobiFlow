from django import forms

class ImportarCSVForm(forms.Form):
    arquivo_csv = forms.FileField(
        label='Selecione o arquivo CSV',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv'})
    )