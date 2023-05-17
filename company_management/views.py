from django.shortcuts import render, redirect
from .models import Company, CompanyBranch
from .forms import CompanyForm, BranchForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


@login_required
def home(request):
    # Pagination 
    p = Paginator(Company.objects.all(), 5)
    page = request.GET.get('page')
    companies = p.get_page(page)
    
    return render(request, 'company_management/index.html', {'companies': companies})

## company 
@login_required
def add_company(request):
    form = CompanyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_company = form.save()
            return redirect('home')
        else:
            messages.error(request, "Não foi possível adicionar. Verifique os dados e tente novamente.")
    return render(request, 'company_management/add_company.html', {'form': form})

@login_required
def edit_company(request, pk):
    company_data = Company.objects.get(id=pk)

    # pagination
    p = Paginator(CompanyBranch.objects.filter(company=pk), 5)
    page = request.GET.get('page')
    company_branches = p.get_page(page)

    #original
    #company_branches = CompanyBranch.objects.filter(company=pk)

    ## Forms
    form = CompanyForm(request.POST or None, instance=company_data)
    branch_form = BranchForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, "Não foi possível editar. Verifique os dados e tente novamente.")
    return render(request, 'company_management/edit_company.html', {'form': form, 'company_branches': company_branches, 'branch_form':branch_form, 'company_id':pk})

@login_required
def delete_company(request, pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return redirect('home')

## branch
@login_required
def add_branch(request):
    branch_form = BranchForm(request.POST or None)
    company_id = request.POST.get('company_id')

    if request.method == "POST":
        if branch_form.is_valid():
            branch_form.instance.company_id = company_id
            branch_form.save()
            return HttpResponse("Success")
        else:
            errors = {}
            for field, error in branch_form.errors.items():
                errors[field] = error.as_text()
            return JsonResponse({'errors': errors}, status=400)

@login_required
def edit_branch(request, pk):
    branch = CompanyBranch.objects.get(id=pk)
    if request.method == "GET":
        data = {
            'id': pk,
            'branch_name': branch.branch_name,
            'status': branch.status,
            'branch_CNPJ': branch.branch_CNPJ,
        }
        return JsonResponse(data)
    elif request.method == "POST":
        branch = CompanyBranch.objects.get(id=pk)
        branch_form = BranchForm(request.POST or None, instance=branch)
        if branch_form.is_valid():
            branch_form.save()
            return HttpResponse("Success")
        else:
            errors = {}
            for field, error in branch_form.errors.items():
                errors[field] = error.as_text()
            return JsonResponse({'errors': errors}, status=400)