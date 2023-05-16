from django import forms
from .models import Company, CompanyBranch

# Add Company
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome da empresa", "class":"form-control"}), label="")
    status = forms.BooleanField(required=False, initial=False,  label="Ativo?", widget=forms.widgets.CheckboxInput(attrs={"class":"form-check-input"}))

    class Meta:
        model = Company
        fields = ['company_name', 'status']
        exclude = ("company",)

class BranchForm(forms.ModelForm):
    branch_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome da filial", "class":"form-control"}), label="Nome da filial")
    branch_CNPJ = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"CNPJ", "class":"form-control"}), label="CNPJ")
    status = forms.BooleanField(required=False, initial=False,  label="Ativo?", widget=forms.widgets.CheckboxInput(attrs={"class":"form-check-input"}))
    
    class Meta:
        model = CompanyBranch
        fields = ['branch_name', 'branch_CNPJ', 'status']
        exclude = ("company_branch",)