from django.shortcuts import render
from menus.models import MenuItem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from menus.forms import MenusForm
from django.urls import reverse_lazy
from menus.models import MenuItem, Cart, CartItem
from django.shortcuts import redirect, get_object_or_404

from django.http import HttpResponseRedirect


def Base(request):
    return render(request, 'menus/base.html')


class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menus/menus_list.html'
    success_url = reverse_lazy('menus:list')


class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenusForm
    template_name = 'menus/menus_form.html'
    success_url = reverse_lazy('menus:list')


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenusForm
    template_name = 'menus/menus_form.html'
    success_url = reverse_lazy('menus:list')


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'menus/menus_delete.html'
    success_url = reverse_lazy('menus:list')


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'menus/menus_detail.html'
    success_url = reverse_lazy('menus:list')


def SearchView(request):
    query = request.GET.get('q', '')
    if query:

        menu_item = MenuItem.objects.filter(
            name__icontains=query) | MenuItem.objects.filter(category__icontains=query)
    else:
        results = MenuItem.objects.none() | menu_item

    return render(request, 'menus/menus_list.html', {'object_list': results})


def add_to_cart(request, id):
    # item = get_object_or_404(MenuItem, pk=item_id)
    # if request.user.is_authenticated:
    #     cart, created = Cart.objects.get_or_create(user=request.user)
    # else:
    #     pass

    # cart.items.add(item)

    # return redirect('menus:list')
    # if request.method == 'POST' and request.is_ajax():
    #     try:
    #         item_id = request.GET.get('id')
    #         item = MenuItem.objects.get(pk=id)
    #         cart, created = Cart.objects.get_or_create(user=request.user)
    #         cart.items.add(item)
    #         return JsonResponse({'success': True})
    #     except Exception as e:
    #         return JsonResponse({'success': False, 'error': str(e)})
    # # else:
    #     return JsonResponse({'success': False, 'error': 'Invalid request method or not AJAX.'})

    item_id = request.GET.get('id')
    item = MenuItem.objects.get(pk=id)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user)
    # cart.items.add(item)
    return HttpResponseRedirect(request.path_info)
    #     except Exception as e:
    #         return JsonResponse({'success': False, 'error': str(e)})
    # # else:
    #     return JsonResponse({'success': False, 'error': 'Invalid request method or not AJAX.'})


def get_cart_count(self, user):
    return CartItem.objects.filter(cart__is__paid=False, cart_user=user).count()
