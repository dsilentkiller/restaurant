from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
