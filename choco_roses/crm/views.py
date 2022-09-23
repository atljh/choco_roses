import json
import environ
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render
from crm.models import (
	Order, RoseColour, RoseAmount, RoseBox, RosePacking, BucketsDetails, OrderStatus, OrderType)
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def is_ajax(request):
	return request.headers.get('x-requested-with') == 'XMLHttpRequest'


@staff_member_required
def index(request):
	orders_list = Order.objects.order_by('-given_date')
	nearest_orders = [order for order in orders_list]

	order_stats = OrderStatus.objects.all()
	orders = {order_status: Order.objects.filter(order_status=order_status) for order_status in order_stats}
	context = {
		'nearest_orders': nearest_orders,
		'all_orders': orders,
	}
	return render(request, 'crm/index.html', context=context)



@staff_member_required
def client_req(request):
	return render(request, 'client.html')


@staff_member_required
def add_client(request):
	return render(request, 'add_client.html')


@staff_member_required
def calendar(request):		
	return render(request, 'crm/calendar.html')





@staff_member_required
def settings(request):
	return render(request, 'crm/settings.html')


@staff_member_required
def todo(request):
	return render(request, 'crm/todo.html')
