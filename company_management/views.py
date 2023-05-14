from django.shortcuts import render
from .models import Company, CompanyBranch

def home(request):
    companies = Company.objects.all()
    return render(request, 'index.html', {'companies': companies})
