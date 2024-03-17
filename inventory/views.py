from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from inventory.forms import PurchaseForm, InventoryForm, KitchenBillForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.forms import formset_factory
from inventory.models import Inventory, PurchaseBill, SendToKitchen, Sales, calculate_inventory_usage, calculate_remaining_quantity_in_kitchen, calculate_remaining_quantity_after_sales
from django.db import models


# def Base(request):
#     return render(request, 'inventory/base.html')


class InventoryItemListView(ListView):
    model = Inventory
    template_name = 'inventory/list.html'
    success_url = reverse_lazy('inventory:list')


class InventoryItemCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/form.html'
    success_url = reverse_lazy('inventory:list')

    def inventory_form(request):
        InventoryForm = formset_factory(InventoryForm, extra=1)
        if request.method == 'POST':
            formset = InventoryForm(request.POST)
            if formset.is_valid():
                for form in formset:
                    form.save()
        else:
            formset = InventoryForm()
        return render(request, 'form.html', {'formset': formset})


class InventoryItemUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/form.html'
    success_url = reverse_lazy('inventory:list')


class InventoryItemDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/delete.html'
    success_url = reverse_lazy('inventory:list')


class InventoryItemDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/detail.html'
    success_url = reverse_lazy('inventory:list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        results = Inventory.objects.filter(
            name__icontains=query) | Inventory.objects.filter(category__name__icontains=query)
    else:
        results = Inventory.objects.none()

    return render(request, 'inventory/list.html', {'object_list': results})

# purchase bill


class PurchaseItemListView(ListView):
    model = PurchaseBill
    template_name = 'inventory/purchase/purchase_bill_list.html'
    success_url = reverse_lazy('inventory:purchase-list')


class PurchaseItemCreateView(CreateView):
    model = PurchaseBill
    form_class = InventoryForm
    template_name = 'purchase/form.html'
    success_url = reverse_lazy('purchase:list')


class PurchaseItemUpdateView(UpdateView):
    model = PurchaseBill
    form_class = PurchaseForm
    template_name = 'purchase/form.html'
    success_url = reverse_lazy('purchase:list')


class PurchaseItemDeleteView(DeleteView):
    model = PurchaseBill
    template_name = 'purchase/delete.html'
    success_url = reverse_lazy('purchase:list')


class PurchaseItemDetailView(DetailView):
    model = PurchaseBill
    template_name = 'purchase/detail.html'
    success_url = reverse_lazy('purchase:list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        results = PurchaseBill.objects.filter(
            name__icontains=query) | PurchaseBill.objects.filter(name__icontains=query)
    else:
        results = PurchaseBill.objects.none()

    return render(request, 'purchase/purchase_bill_list.html', {'object_list': results})


# kitchen bill

class KitchenItemListView(ListView):
    model = PurchaseBill
    template_name = 'inventory/kitchen/kitchen_bill_list.html'
    success_url = reverse_lazy('inventory:kitchen-bill-list')


class KitchenItemCreateView(CreateView):
    model = SendToKitchen
    form_class = KitchenBillForm
    template_name = 'inventory/kitchen/kitchen_bill_form.html'
    success_url = reverse_lazy('inventory:kitchen-bill-list')


class KitchenItemUpdateView(UpdateView):
    model = SendToKitchen
    form_class = KitchenBillForm
    template_name = 'inventory/kitchen/kitchen_bill_form.html'
    success_url = reverse_lazy('inventory:kitchen-bill-list')


class KitchenItemDeleteView(DeleteView):
    model = SendToKitchen
    template_name = 'inventory/kitchen/kitchen_bill_delete.html'
    success_url = reverse_lazy('inventory:kitchen-bill-list')


class KitchenItemDetailView(DetailView):
    model = SendToKitchen
    template_name = 'inventory/kitchen/kitchen_bill_detail.html'
    success_url = reverse_lazy('inventory:kitchen-bill-list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        results = SendToKitchen.objects.filter(
            name__icontains=query) | SendToKitchen.objects.filter(category__icontains=query)
    else:
        results = SendToKitchen.objects.none()

    return render(request, 'inventory/kitchen/kitchen_bill_list.html', {'object_list': results})


def inventory_dashboard(request):
    total_usage = calculate_inventory_usage()
    remaining_in_kitchen = calculate_remaining_quantity_in_kitchen()
    remaining_after_sales = calculate_remaining_quantity_after_sales()
    return render(request, 'inventory/inventory-dashboard.html', {
        'total_usage': total_usage,
        'remaining_in_kitchen': remaining_in_kitchen,
        'remaining_after_sales': remaining_after_sales
    })


def calculate_total_sales():
    total_sales = Sales.objects.aggregate(
        total=models.Sum('quantity'))['total']
    return total_sales or 0


def inventory_sales_report(request):

    inventory_items = Inventory.objects.all()  # retrive all INventory items
    report_data = {}  # to store sales and stock data
    for item in inventory_items:
        total_sales_for_item = Sales.objects.filter(name=item).aggregate(
            total=models.Sum('quantity'))['total'] or 0
        # retrive total sale for current inventory item
        remaining_stock = item.quantity - total_sales_for_item
        report_data[item.name] = {
            'total_sales': total_sales_for_item,
            'remaining_stock': remaining_stock
        }

    return render(request, 'inventory/inventory_report.html', {'report_data': report_data})
