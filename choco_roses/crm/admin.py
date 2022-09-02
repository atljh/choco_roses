from django.contrib import admin
from .models import Client, Product, Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails, OrderType,\
	OrderStatus


admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(RoseColour)
admin.site.register(RoseAmount)
admin.site.register(RoseBoxes)
admin.site.register(RosePacking)
admin.site.register(BucketsDetails)
admin.site.register(OrderType)
admin.site.register(OrderStatus)
