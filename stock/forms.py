from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
class SearchForm(forms.Form):
    company = forms.CharField(label='Search Word')

    def clean_company(self):
        data = self.cleaned_data['company']

        # Check if a search word is string
        return data


