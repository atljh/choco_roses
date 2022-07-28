from django.contrib import admin
from .models import Client, Product, Order, RoseColor, RoseAmount


admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(RoseColor)
admin.site.register(RoseAmount)
