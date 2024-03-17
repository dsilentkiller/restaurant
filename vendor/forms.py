from django import forms
from vendor.models import Vendor
from django.db import models


class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor
        verbose_name = 'vendor_form'
        verbose_name_plural = 'vendor_forms'
        fields = '__all__'
