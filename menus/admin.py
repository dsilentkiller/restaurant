from django.contrib import admin
from menus.models import MenuItem, Category, Receipe, CartItem, Cart
# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Receipe)
admin.site.register(CartItem)
admin.site.register(Cart)
