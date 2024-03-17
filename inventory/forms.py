from inventory.models import Inventory, PurchaseBill, SendToKitchen
from django import forms


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('__all__')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseBill
        fields = ('__all__')


class KitchenBillForm(forms.ModelForm):
    class Meta:
        model = SendToKitchen
        fields = ('__all__')
