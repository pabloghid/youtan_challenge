from django.db import models
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.company_name

class CompanyBranch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)
    branch_CNPJ = models.CharField(max_length=14, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)