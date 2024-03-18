from django.db import models
from menus.models import Category
from vendor.models import Vendor


class PurchaseBill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=100, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField()
    quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class SendToKitchen(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Sales(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


def calculate_inventory_usage():
    # Calculate total quantity used from the kitchen
    total_usage = SendToKitchen.objects.aggregate(
        total=models.Sum('quantity'))['total']
    return total_usage or 0


def calculate_remaining_quantity_in_kitchen():
    # Calculate remaining quantity in the kitchen
    initial_quantity_sent_to_kitchen = SendToKitchen.objects.aggregate(
        total=models.Sum('quantity'))['total']
    total_usage = calculate_inventory_usage()
    remaining_quantity = initial_quantity_sent_to_kitchen - total_usage
    return remaining_quantity


def calculate_remaining_quantity_after_sales():
    # Calculate remaining quantity after sales
    initial_quantity_in_kitchen = SendToKitchen.objects.aggregate(
        total=models.Sum('quantity'))['total']
    total_sales = Inventory.objects.aggregate(
        total=models.Sum('quantity'))['total']
    remaining_quantity_in_kitchen = calculate_remaining_quantity_in_kitchen()
    remaining_quantity = remaining_quantity_in_kitchen - total_sales
    return remaining_quantity


def calculate_total_sales():
    total_sales = Sales.objects.aggregate(
        total=models.Sum('quantity'))['total']
    return total_sales or 0


def calculate_remaining_quantity_after_sales():
    # Calculate remaining quantity after sales
    initial_quantity_in_kitchen = SendToKitchen.objects.aggregate(
        total=models.Sum('quantity'))['total']
    # Call the function to get the total sales
    total_sales = calculate_total_sales()
    remaining_quantity_in_kitchen = calculate_remaining_quantity_in_kitchen()
    remaining_quantity = remaining_quantity_in_kitchen - total_sales
    return remaining_quantity
