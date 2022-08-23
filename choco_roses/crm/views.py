import json
import environ
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from main.models import (
	Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails)


env = environ.Env()
environ.Env.read_env()


@staff_member_required
def index(request):
	return render(request, 'crm/index.html')


# region orders


@staff_member_required
def orders_req(request):
	from django.core.paginator import Paginator

	orders = Order.objects.all()
	paginator = Paginator(orders, 3)

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

	return render(request, 'crm/order-edit.html', context=context)


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

		# Save edited Order model
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

		order_model.save()


		# Get orders buckets from request and serialize from json
		buckets = json.loads(request.POST.get('buckets'))
		# Get existed order buckets
		buckets_model = BucketsDetails.objects.filter(order_id=order_model.id)

		"""
		Save BucketsDetails model
		"""
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
		# Order details
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

		# Save Order model
		order_model = Order.objects.create(
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

		# Get orders buckets from request and serialize from json
		buckets = json.loads(request.POST.get('buckets'))

		"""
		Save BucketsDetails model
		"""
		for bucket in buckets:
			bucket_colours = bucket.get('colours')
			colours = ''
			for colour in bucket_colours:
				colours += f'{colour} '
			bucket_model = BucketsDetails.objects.create(
				order_id=order.id,
				colours=colours,
				rose_amount=bucket.get('rose_amount'),
				packing=bucket.get('packing'),
				rose_box=bucket.get('rose_box'),
				price=bucket.get('price'),
			)


	order = json.loads(request.POST.get('order'))
	order_model = Order.objects.get(number=order.get('number', 'None'))

	if order_model:
		update_order(order, order_model)
	else:
		save_new(order)


	return render(request, 'crm/index.html')


@staff_member_required
def edit_order(request, order_number):
	order = Order.objects.get(number=order_number)
	buckets = BucketsDetails.objects.get(order_id=order.id)

	# total_price = request.POST.get('total_price', 'None')
	# name_surname = request.POST.get('name_surname', 'None')
	# instagram = request.POST.get('instagram', 'None')
	# from_where = request.POST.get('from_where', 'None')
	# address = request.POST.get('address', 'None')
	# phone = request.POST.get('phone', 'None')
	# order_type = request.POST.get('order_type', 'None')
	# order_status = request.POST.get('order_status', 'None')
	# anonymous = request.POST.get('anonymous', 'False')
	# first_order = request.POST.get('first_order', 'False')
	# delivery_data = request.POST.get('delivery_data', 'None')
	# pickup_data = request.POST.get('pickup_data', 'None')
	# payment = request.POST.get('payment', 'None')
	# description = request.POST.get('description', 'None')
	#
	# # Save edited Order model
	# order.total_price = total_price
	# order.name_surname = name_surname
	# order.instagram = instagram
	# order.from_where = from_where
	# order.address = address
	# order.phone = phone
	# order.order_type = order_type
	# order.order_status = order_status
	# order.anonymous = anonymous
	# order.first_order = first_order
	# order.delivery_data = delivery_data
	# order.pickup_data = pickup_data
	# order.payment = payment
	# order.description = description
	#
	# order.save()
	#
	# colour1 = request.POST.get('colour1', 'None')
	# colour2 = request.POST.get('colour2', 'None')
	# colour3 = request.POST.get('colour3', 'None')
	# colour4 = request.POST.get('colour4', 'None')
	# colour5 = request.POST.get('colour5', 'None')
	# colour6 = request.POST.get('colour6', 'None')
	# colour7 = request.POST.get('colour7', 'None')
	# rose_amount = request.POST.get('rose_amount', 'None')
	# packing = request.POST.get('packing', 'None')
	# rose_box = request.POST.get('box', 'None')
	# price = request.POST.get('price', 'None')
	#
	# # Save BucketDetails model
	# buckets.rose_amount = rose_amount
	# buckets.packing = packing
	# buckets.rose_box = rose_box
	# buckets.price = price
	#
	# buckets.save()

	return redirect(f'/crm/order/{order_number}/')


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
