import environ
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from main.models import (
	Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails)
import json

env = environ.Env()
environ.Env.read_env()


@staff_member_required
def index(request):
	# create_product = Product.objects.create(name=name, price=price, color=color, amount=amount, descriprion)
	# create_amount = RoseAmount.objects.create(amount=amount)

	return render(request, 'crm/index.html')


# region orders


@staff_member_required
def orders_req(request):
	orders = Order.objects.all()
	for order in orders:
		print(order.order_status)
	context = {
		'orders': orders,
	}
	return render(request, 'crm/orders.html', context=context)


@staff_member_required
def order_req(request, order_id):
	order = Order.objects.get(id=order_id)
	buckets = BucketsDetails.objects.get(order_id=order.id)
	colours = RoseColour.objects.all()
	rose_amount = RoseAmount.objects.all()
	boxes = RoseBoxes.objects.all()
	rose_packing = RosePacking.objects.all()

	print(order.id)

	context = {
		'colours': colours,
		'rose_amount': rose_amount,
		'boxes': boxes,
		'rose_packing': rose_packing,
		'order': order,
		'buckets': buckets,
	}
	return render(request, 'crm/order-edit.html', context=context)


@staff_member_required
def client_req(request):
	return render(request, 'client.html')


@staff_member_required
def add_order(request):
	colours = RoseColour.objects.all()
	rose_amount = RoseAmount.objects.all()
	boxes = RoseBoxes.objects.all()
	rose_packing = RosePacking.objects.all()
	context = {
		'colours': colours,
		'rose_amount': rose_amount,
		'boxes': boxes,
		'rose_packing': rose_packing
	}

	return render(request, 'crm/add_order.html', context=context)


@staff_member_required
def save_order(request):

	# Get order data from request and serialize
	order = json.loads(request.POST.get('order'))

	# Order details
	number = order.get('number', 'None')
	total_price = order.get('total_price', 'None')
	name_surname = order.get('name_surname', 'None')
	instagram = order.get('instagram', 'None')
	from_where = order.get('from_where', 'None')
	address = order.get('address', 'None')
	phone = order.get('phone', 'None')
	order_type = order.get('order_type', 'None')
	order_status = order.get('order_status', 'None')
	anonymous = order.get('anonymous', 'False')
	first_order = order.get('first_order', 'False')
	delivery_data = order.get('delivery_data', 'None')
	pickup_data = order.get('pickup_data', 'None')
	payment = order.get('payment', 'None')
	description = order.get('description', 'None')

	# Save Order model
	# order = Order.objects.create(
	# 	number=number,
	# 	total_price=total_price,
	# 	name_surname=name_surname,
	# 	instagram=instagram,
	# 	from_where=from_where,
	# 	address=address,
	# 	phone=phone,
	# 	order_type=order_type,
	# 	order_status=order_status,
	# 	anonymous=bool(anonymous),
	# 	first_order=bool(first_order),
	# 	delivery_data=delivery_data,
	# 	pickup_data=pickup_data,
	# 	payment=payment,
	# 	created_by=str(request.user),
	# 	description=description
	# )


	# Get orders buckets from request and serialize from json
	buckets = json.loads(request.POST.get('buckets'))


	"""
	Save BucketsDetails model
	"""
	# for bucket in buckets:
	# 	bucket_colours = bucket.get('colours')
	# 	colours = ''
	# 	for colour in bucket_colours:
	# 		colours += f'{colour} '
	# 	bucket_model = BucketsDetails.objects.create(
	# 		order_id=order.id,
	# 		colours=colours,
	# 		rose_amount=bucket.get('rose_amount'),
	# 		packing=bucket.get('packing'),
	# 		rose_box=bucket.get('rose_box'),
	# 		price=bucket.get('price'),
	# 	)

	return redirect('/crm/')


def add_bucket(request):
	buckets = json.loads(request.POST.get('buckets'))
	order = json.loads(request.POST.get('order'))
	# for bucket in buckets:
	# 	colours = [colour for colour in bucket.get('colours')]
	# 	rose_amount = bucket.get('rose_amount')
	# 	packing = bucket.get('packing')
	# 	rose_box = bucket.get('rose_box')
	# 	price = bucket.get('price')
	# 	print(f'Букет номер {data.index(bucket)+1}:')
	# 	print("Цвета: ", colours)
	# 	print("Кол-во роз: ", rose_amount)
	# 	print("Упаковка: ", rose_amount)
	# 	print("Коробка: ", rose_box)
	# 	print("Цена: ", price)

	return JsonResponse({"response": 'good'}, status=200)


@staff_member_required
def edit_order(request, order_id):
	order = Order.objects.get(id=order_id)
	buckets = BucketsDetails.objects.get(order_id=order.id)
	# buckets_colours = BucketsColours.objects.get(bucket_id=buckets.id)

	total_price = request.POST.get('total_price', 'None')
	name_surname = request.POST.get('name_surname', 'None')
	instagram = request.POST.get('instagram', 'None')
	from_where = request.POST.get('from_where', 'None')
	address = request.POST.get('address', 'None')
	phone = request.POST.get('phone', 'None')
	order_type = request.POST.get('order_type', 'None')
	order_status = request.POST.get('order_status', 'None')
	anonymous = request.POST.get('anonymous', 'False')
	first_order = request.POST.get('first_order', 'False')
	delivery_data = request.POST.get('delivery_data', 'None')
	pickup_data = request.POST.get('pickup_data', 'None')
	payment = request.POST.get('payment', 'None')
	description = request.POST.get('description', 'None')

	# Save edited Order model
	order.total_price = total_price
	order.name_surname = name_surname
	order.instagram = instagram
	order.from_where = from_where
	order.address = address
	order.phone = phone
	order.order_type = order_type
	order.order_status = order_status
	order.anonymous = anonymous
	order.first_order = first_order
	order.delivery_data = delivery_data
	order.pickup_data = pickup_data
	order.payment = payment
	order.description = description

	order.save()

	colour1 = request.POST.get('colour1', 'None')
	colour2 = request.POST.get('colour2', 'None')
	colour3 = request.POST.get('colour3', 'None')
	colour4 = request.POST.get('colour4', 'None')
	colour5 = request.POST.get('colour5', 'None')
	colour6 = request.POST.get('colour6', 'None')
	colour7 = request.POST.get('colour7', 'None')
	rose_amount = request.POST.get('rose_amount', 'None')
	packing = request.POST.get('packing', 'None')
	rose_box = request.POST.get('box', 'None')
	price = request.POST.get('price', 'None')

	# Save BucketDetails model
	buckets.rose_amount = rose_amount
	buckets.packing = packing
	buckets.rose_box = rose_box
	buckets.price = price

	buckets.save()

	# Save BucketsColours model
	# buckets_colours.colour1 = colour1
	# buckets_colours.colour2 = colour2
	# buckets_colours.colour3 = colour3
	# buckets_colours.colour4 = colour4
	# buckets_colours.colour5 = colour5
	# buckets_colours.colour6 = colour6
	# buckets_colours.colour7 = colour7
	#
	# buckets_colours.save()

	return redirect(f'/crm/order/{order_id}/')


@staff_member_required
def delete_order(request, order_id):
	order = Order.objects.get(id=order_id)
	order.delete()


# endregion

def add_client(request):
	return render(request, 'add_client.html')
