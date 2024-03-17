from django.shortcuts import render

from django.shortcuts import render
from vendor.models import Vendor
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from vendor.forms import VendorForm
from django.urls import reverse_lazy


class VendorListView(ListView):
    model = Vendor
    template_name = 'Vendor/Vendor_list.html'
    success_url = reverse_lazy('Vendor:list')


class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'Vendor/Vendor_form.html'
    success_url = reverse_lazy('Vendor:list')


class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'Vendor/Vendor_form.html'
    success_url = reverse_lazy('Vendor:list')


class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'Vendor/Vendor_delete.html'
    success_url = reverse_lazy('Vendor:list')


class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'Vendor/Vendor_detail.html'
    success_url = reverse_lazy('Vendor:list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        menu_item = Vendor.objects.filter(
            name__icontains=query) | Vendor.objects.filter(category__icontains=query)
    else:
        results = Vendor.objects.none() | menu_item

    return render(request, 'Vendor/Vendor_list.html', {'object_list': results})
