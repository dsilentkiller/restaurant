from django import forms
from order.models import Order
from django.db import models


class OrderForm(forms.ModelForm):

    def __str__(self):
        pass

    class Meta:
        model = Order
        verbose_name = 'orderform'
        verbose_name_plural = 'orderforms'
        fields = '__all__'
