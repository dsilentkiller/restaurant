from django.shortcuts import render
from order.models import Order
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from order.forms import OrderForm
from django.urls import reverse_lazy
from django.http import HttpResponse


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    success_url = reverse_lazy('order:list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order:list')


def handle_form_submission(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        table_no = request.POST.get('table_no')
        waiter = request.POST.get('waiter')
        price = request.POST.get('price')
        order = Order(item_name, item_name, quantity=quantity,
                      table_no=table_no, waiter=waiter, price=price)
        return render(request, "Form submitted successfully!", 'order/order_list.html', {'order': order})

    else:
        # Handle GET request (if needed)
        return HttpResponse("This URL only accepts POST requests.")


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order:list')


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_delete.html'
    success_url = reverse_lazy('order:list')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    success_url = reverse_lazy('order:list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        menu_item = Order.objects.filter(
            name__icontains=query) | Order.objects.filter(category__icontains=query)
    else:
        results = Order.objects.none() | menu_item

    return render(request, 'Order/Order_list.html', {'object_list': results})
