from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)

class CompanyBranch(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)