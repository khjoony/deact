from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class KospiSearchForm(forms.Form):
    name = forms.CharField(label='Search Word', required=False)
    def clean_name(self):
        cleaned_name = self.cleaned_data['name']

        # Check if a search word is string
        if not self.additional_validate(cleaned_name):
            raise forms.ValidationError(
                self.error_messages['name_incorrect'], code='name_incorrect',
            )
        return cleaned_name


class KosdakSearchForm(forms.Form):
    name = forms.CharField(label='Search Word', required=False)
    def clean_name(self):
        cleaned_name = self.cleaned_data['name']

        # Check if a search word is string
        if not self.additional_validate(cleaned_name):
            raise forms.ValidationError(
                self.error_messages['name_incorrect'], code='name_incorrect',
            )
        return cleaned_name
