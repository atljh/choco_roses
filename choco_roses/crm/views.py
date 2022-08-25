import json
import environ
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from main.models import (
	Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails)
from django.core.paginator import Paginator
import datetime

"""
TODO: Убрать глобальные переменные
Написать логику отдельно
Дописать ReadMe
"""
env = environ.Env()
environ.Env.read_env()


@staff_member_required
def index(request):

	needed = Order.objects.filter(order_status='Нужно сделать')
	process = Order.objects.filter(order_status='В процессе')
	packed = Order.objects.filter(order_status='Упакован')
	way = Order.objects.filter(order_status='В пути')
	done = Order.objects.filter(order_status='Отдан')

	orders_list = Order.objects.order_by('-given_date')
	nearest_orders = [order for order in orders_list]

	context = {
		'needed': needed,
		'process': process,
		'packed': packed,
		'way': way,
		'done': done,
		'nearest_orders': nearest_orders
	}

	return render(request, 'crm/index.html', context=context)


# region orders


@staff_member_required
def orders_req(request):

	orders = Order.objects.all()

	paginator = Paginator(orders, 10)
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)
	page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

	context = {
		'page_obj': page_obj
	}
	return render(request, 'crm/orders.html', context=context)


@staff_member_required
def order_req(request, order_number):
	order = Order.objects.get(number=order_number)
	buckets = BucketsDetails.objects.filter(order_id=order.id)
	colours = RoseColour.objects.all()
	rose_amount = RoseAmount.objects.all()
	boxes = RoseBoxes.objects.all()
	rose_packing = RosePacking.objects.all()

	bucket_colours = [bucket.colours.split() for bucket in buckets]


	context = {
		'colours': colours,
		'rose_amount': rose_amount,
		'boxes': boxes,
		'rose_packing': rose_packing,
		'order': order,
		'buckets': zip(buckets, bucket_colours),
		'bucket_colours': bucket_colours
	}

	return render(request, 'crm/order.html', context=context)


@staff_member_required
def add_order(request):
	colours = RoseColour.objects.all()
	rose_amount = RoseAmount.objects.all()
	boxes = RoseBoxes.objects.all()
	rose_packing = RosePacking.objects.all()
	last_order_num = Order.objects.last().number + 1

	context = {
		'colours': colours,
		'rose_amount': rose_amount,
		'boxes': boxes,
		'rose_packing': rose_packing,
		'last_order_num': last_order_num
	}

	return render(request, 'crm/add_order.html', context=context)


@staff_member_required
def save_order(request):

	def update_order(order, order_model):
		number = order.get('number', 'None')
		total_price = order.get('total_price', 'None')
		name_surname = order.get('name_surname', 'None')
		instagram = order.get('instagram', 'None')
		from_where = order.get('from_where', 'None')
		address = order.get('address', 'None')
		phone = order.get('phone', 'None')
		order_type = order.get('order_type', 'None')
		order_status = order.get('order_status')
		anonymous = order.get('anonymous', 'False')
		first_order = order.get('first_order', 'False')
		delivery_data = order.get('delivery_data', 'None')
		pickup_data = order.get('pickup_data', 'None')
		payment = order.get('payment', 'None')
		description = order.get('description', 'None')
		given_date_raw = order.get('given_date', 'None')
		date_format = "%H:%M %d/%m/%Y"
		given_date = datetime.datetime.strptime(given_date_raw, date_format)

		order_model.number = number
		order_model.total_price = total_price
		order_model.name_surname = name_surname
		order_model.instagram = instagram
		order_model.from_where = from_where
		order_model.address = address
		order_model.phone = phone
		order_model.order_type = order_type
		order_model.order_status = order_status
		order_model.anonymous = anonymous
		order_model.first_order = first_order
		order_model.delivery_data = delivery_data
		order_model.pickup_data = pickup_data
		order_model.payment = payment
		order_model.description = description
		order_model.given_date = given_date

		order_model.save()


		buckets = json.loads(request.POST.get('buckets'))
		buckets_model = BucketsDetails.objects.filter(order_id=order_model.id)


		for bucket, bucket_model in zip(buckets, buckets_model):
			bucket_colours = bucket.get('colours')
			rose_amount = bucket.get('rose_amount', 'None')
			packing = bucket.get('packing', '')
			rose_box = bucket.get('box', '')
			price = bucket.get('price', 'None')
			colours = ''
			for colour in bucket_colours:
				colours += f'{colour} '

			bucket_model.colours = colours
			bucket_model.rose_amount = rose_amount
			bucket_model.packing = packing
			bucket_model.rose_box = rose_box
			bucket_model.price = price
			bucket_model.save()


	def save_new(order):
		number = order.get('number', 'None')
		total_price = order.get('total_price', 'None')
		name_surname = order.get('name_surname', 'None')
		instagram = order.get('instagram',)
		from_where = order.get('from_where')
		address = order.get('address', 'None')
		phone = order.get('phone', 'None')
		order_type = order.get('order_type', 'None')
		order_status = order.get('order_status')
		anonymous = order.get('anonymous', 'False')
		first_order = order.get('first_order', 'False')
		delivery_data = order.get('delivery_data', 'None')
		pickup_data = order.get('pickup_data', 'None')
		payment = order.get('payment', 'None')
		description = order.get('description', 'None')

		new_order_model = Order.objects.create(
			number=number,
			total_price=total_price,
			name_surname=name_surname,
			instagram=instagram,
			from_where=from_where,
			address=address,
			phone=phone,
			order_type=order_type,
			order_status=order_status,
			anonymous=bool(anonymous),
			first_order=bool(first_order),
			delivery_data=delivery_data,
			pickup_data=pickup_data,
			payment=payment,
			created_by=str(request.user),
			description=description
		)

		buckets = json.loads(request.POST.get('buckets'))

		for bucket in buckets:
			bucket_colours = bucket.get('colours')
			colours = ''
			for colour in bucket_colours:
				colours += f'{colour} '
			new_bucket_model = BucketsDetails.objects.create(
				order_id=new_order_model.id,
				colours=colours,
				rose_amount=bucket.get('rose_amount'),
				packing=bucket.get('packing'),
				rose_box=bucket.get('rose_box'),
				price=bucket.get('price'),
			)


	order = json.loads(request.POST.get('order'))

	try:
		order_model = Order.objects.get(number=order.get('number', 'None'))
		update_order(order, order_model)
	except Order.DoesNotExist:
		save_new(order)


	return render(request, 'crm/index.html')


@staff_member_required
def delete_order(request, order_id):
	order = Order.objects.get(id=order_id)
	order.delete()


# endregion


@staff_member_required
def client_req(request):
	return render(request, 'client.html')


def add_client(request):
	return render(request, 'add_client.html')
