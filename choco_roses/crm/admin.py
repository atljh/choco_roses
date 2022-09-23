from django.contrib import admin
from .models import Client, Order, RoseColour, RoseAmount, RoseBox, RosePacking, BucketsDetails, OrderType,\
	OrderStatus, Product


admin.site.register(Order)
admin.site.register(Client)
admin.site.register(RoseColour)
admin.site.register(RoseAmount)
admin.site.register(RoseBox)
admin.site.register(RosePacking)
admin.site.register(BucketsDetails)
admin.site.register(OrderType)
admin.site.register(OrderStatus)
admin.site.register(Product)