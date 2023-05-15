from django import forms
from .models import Company

# Add Company
class AddCompanyForm(forms.ModelForm):
    company_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Company name", "class":"form-control"}), label="")
    status = forms.BooleanField(required=False, initial=False,  label="Ativo?", widget=forms.widgets.CheckboxInput(attrs={"class":"form-check-input"}))

    class Meta:
        model = Company
        fields = ['company_name', 'status']
        exclude = ("company",)