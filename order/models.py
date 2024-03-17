from django.db import models
from menus.models import MenuItem
from vendor.models import Waiter


class Table(models.Model):
    name = models.CharField(max_length=50)
    floor = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}-{self.floor}"


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True)
    item_name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    table_no = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.item_name}-{self.quantity}"
