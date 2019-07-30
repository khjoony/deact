from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class KospiSearchForm(forms.Form):
    company_code = forms.IntegerField(min_value=0, max_value=100000, required=False)
    company_name = forms.CharField(label='Search Word', required=False)
    """
    def clean_company_code(self):
        cleaned_company_code = self.cleaned_data['company_code']

        # Check if a search word is string
        if not self.additional_validate(cleaned_company_code):
            raise forms.ValidationError(
                self.error_messages['company_code_incorrect'], code='company_code_incorrect',
            )
        return cleaned_company_code
    """
    def clean_company_name(self):
        cleaned_company_name = self.cleaned_data['company_name']

        # Check if a search word is string
        if not self.additional_validate(cleaned_company_name):
            raise forms.ValidationError(
                self.error_messages['company_name_incorrect'], code='company_name_incorrect',
            )
        return cleaned_company_name


class KosdakSearchForm(forms.Form):
    company_code = forms.IntegerField(min_value=0, max_value=100000, required=False)
    company_name = forms.CharField(label='Search Word', required=False)
    """
    def clean_company_code(self):
        cleaned_company_code = self.cleaned_data['company_code']

        # Check if a search word is string
        if not self.additional_validate(cleaned_company_code):
            raise forms.ValidationError(
                self.error_messages['company_code_incorrect'], code='company_code_incorrect',
            )
        return cleaned_company_code
    """
    def clean_company_name(self):
        cleaned_company_name = self.cleaned_data['company_name']

        # Check if a search word is string
        if not self.additional_validate(cleaned_company_name):
            raise forms.ValidationError(
                self.error_messages['company_name_incorrect'], code='company_name_incorrect',
            )
        return cleaned_company_name
