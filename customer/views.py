
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from customer.forms import CustomerForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.forms import formset_factory
from customer.models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/list.html'
    success_url = reverse_lazy('Customer:list')


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/form.html'
    success_url = reverse_lazy('Customer:list')

    # def Customer_form(request):
    #     CustomerForm = formset_factory(CustomerForm, extra=1)
    #     if request.method == 'POST':
    #         formset = CustomerForm(request.POST)
    #         if formset.is_valid():
    #             for form in formset:
    #                 form.save()
    #     else:
    #         formset = CustomerForm()
    #     return render(request, 'form.html', {'formset': formset})


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/form.html'
    success_url = reverse_lazy('Customer:list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/delete.html'
    success_url = reverse_lazy('Customer:list')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/detail.html'
    success_url = reverse_lazy('Customer:list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        results = Customer.objects.filter(
            name__icontains=query) | Customer.objects.filter(name__icontains=query)
    else:
        results = Customer.objects.none()

    return render(request, 'customer/list.html', {'object_list': results})
