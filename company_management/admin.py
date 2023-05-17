from django.contrib import admin
from .models import Company, CompanyBranch

class ListCompanies(admin.ModelAdmin):
    list_display = ("id", "company_name", "status")
    list_display_links = ("id", "company_name")
    search_fields = ("company_name",)
    list_per_page = 10

class ListCompanyBranches(admin.ModelAdmin):
    list_display = ("branch_name", "company", "status", "branch_CNPJ")
    list_display_links = ("branch_name",)
    search_fields = ("branch_name",)
    list_per_page = 10

admin.site.register(Company, ListCompanies)
admin.site.register(CompanyBranch, ListCompanyBranches)