from django.contrib import admin
from .models import Customer, Tags, Order, Product
admin.site.register(Customer)
admin.site.register(Tags)
admin.site.register(Order)
admin.site.register(Product)