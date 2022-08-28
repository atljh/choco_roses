from datetime import datetime
from main.models import Order, BucketsDetails
import json



def order():
	pass


def delete_order():
	pass


def save_new_order(order, buckets, user):
	number = order.get('number', 'None')
	total_price = order.get('total_price', 'None')
	name_surname = order.get('name_surname', 'None')
	instagram = order.get('instagram', )
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
		created_by=str(user),
		description=description
	)

	for bucket in buckets:
		bucket_colours = bucket.get('colours')
		colours = ''
		for colour in bucket_colours:
			colours += f'{colour} '
		bucket_model = BucketsDetails.objects.create(
			order_id=new_order_model.id,
			colours=colours,
			rose_amount=bucket.get('rose_amount'),
			packing=bucket.get('packing'),
			rose_box=bucket.get('rose_box'),
			price=bucket.get('price'),
		)



def update_order(order, order_model, buckets):
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
	given_date = datetime.strptime(given_date_raw, date_format)

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
