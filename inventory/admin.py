from django.contrib import admin
from .models import Inventory, PurchaseBill, SendToKitchen, Sales

admin.site.register(Inventory)
admin.site.register(PurchaseBill)
admin.site.register(SendToKitchen)
admin.site.register(Sales)
