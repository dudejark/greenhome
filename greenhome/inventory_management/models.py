from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    item = models.ForeignKey(Item, related_name='stock_histories', on_delete=models.CASCADE)
    quantity_change = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.quantity_change}"
