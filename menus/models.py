from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Receipe(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    unit = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='static', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    receipe = models.ManyToManyField(
        Receipe)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"CartItem - {self.menu_item.name} ({self.quantity})"
