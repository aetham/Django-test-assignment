from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_quantity = models.PositiveIntegerField()
    client_id = models.PositiveIntegerField()

    def __str__(self):
        return "Product id: " + str(self.product_id) + " Product name: " + self.product_name + " Quantity: " + \
               str(self.product_quantity) + " Client ID: " + str(self.client_id)
