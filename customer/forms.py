from customer.models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('__all__')
