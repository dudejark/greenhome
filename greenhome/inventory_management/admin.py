from django.contrib import admin

# Register your models here.
from .models import Supplier, Category, Item, StockHistory

admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(StockHistory)
