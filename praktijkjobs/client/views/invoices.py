from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.files.storage import default_storage

from ..models import *

@login_required
def invoices(request):
    invoices = Invoice.objects.filter(created_by=request.user)
    template = "portal/invoices.html"
    context = {
        "invoices": invoices
    }
    return render(request, template, context)

@login_required
def create_invoice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        descriptions = request.POST.getlist('descriptions[]')
        amounts = request.POST.getlist('amounts[]')

        if title and descriptions and amounts:
            invoice = Invoice.objects.create(title=title, created_by=request.user)
            for desc, amt in zip(descriptions, amounts):
                InvoiceItem.objects.create(invoice=invoice, description=desc, amount=amt)
            return redirect('invoices')
    

# @login_required
# def create_invoice(request):
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST)
#         if form.is_valid():
#             invoice = form.save(commit=False)
#             invoice.created_by = request.user
#             invoice.save()
#             return redirect('invoice_list')
#     else:
#         form = InvoiceForm()
#     return render(request, 'portal/invoice_form.html', {'form': form})

# @login_required
# def edit_invoice(request, pk):
#     invoice = get_object_or_404(Invoice, pk=pk, created_by=request.user)
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST, instance=invoice)
#         if form.is_valid():
#             form.save()
#             return redirect('invoice_list')
#     else:
#         form = InvoiceForm(instance=invoice)
#     return render(request, 'portal/invoice_form.html', {'form': form})

# @login_required
# def delete_invoice(request, pk):
#     invoice = get_object_or_404(Invoice, pk=pk, created_by=request.user)
#     if request.method == 'POST':
#         invoice.delete()
#         return redirect('invoice_list')
#     return render(request, 'portal/confirm_delete.html', {'invoice': invoice})
