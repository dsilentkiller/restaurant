from django import forms
from menus.models import MenuItem
from django.db import models


class MenusForm(forms.ModelForm):

    def __str__(self):
        pass

    class Meta:
        model = MenuItem
        verbose_name = 'MenusForm'
        verbose_name_plural = 'MenusForms'
        fields = '__all__'
