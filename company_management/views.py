from django.shortcuts import render, redirect
from .models import Company, CompanyBranch
from .forms import AddCompanyForm

def home(request):
    companies = Company.objects.all()
    return render(request, 'index.html', {'companies': companies})

def add_company(request):
    form = AddCompanyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_company = form.save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})

def edit_company(request, pk):
    company_data = Company.objects.get(id=pk)
    form = AddCompanyForm(request.POST or None, instance=company_data)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit_company.html', {'form': form})

def delete_company(request, pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return redirect('home')