from datetime import datetime
from crm.models import Order, BucketsDetails
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from itertools import chain



def order():
	pass


def delete_order():
	pass


def save_new_order(order, buckets, user, images):
	order_values = {'created_by': str(user)}
	for field in order:
		if field == 'given_date':
			date_format = "%H:%M %d/%m/%Y"
			order_values[field] = datetime.strptime(order.get(f'{field}'), date_format)
			continue
		elif field == 'anonymous' or field == 'first_order':
			order_values[field] = bool(order.get(f'{field}'))
			continue

		order_values[field] = order.get(f'{field}', '')
	new_order_model = Order.objects.create(**order_values)

	# number = order.get('number', 'None')
	# total_price = order.get('total_price', 'None')
	# name_surname = order.get('name_surname', 'None')
	# instagram = order.get('instagram', )
	# from_where = order.get('from_where')
	# address = order.get('address', 'None')
	# phone = order.get('phone', 'None')
	# order_type = order.get('order_type', 'None')
	# order_status = order.get('order_status')
	# anonymous = order.get('anonymous', 'False')
	# first_order = order.get('first_order', 'False')
	# payment = order.get('payment', 'None')
	# description = order.get('description', 'None')
	# given_date_raw = order.get('given_date', 'None')
	# date_format = "%H:%M %d/%m/%Y"
	# given_date = datetime.strptime(given_date_raw, date_format)
	#
	# new_order_model = Order.objects.create(
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
	# 	given_date=given_date,
	# 	payment=payment,
	# 	created_by=str(user),
	# 	description=description,
	#
	# )
	for bucket in buckets:
		bucket_values = {'order_id': new_order_model.id}
		for field in bucket:
			if field == 'colours':
				bucket_colours = bucket.get('colours')
				colours = ''
				for colour in bucket_colours:
					colours += f'{colour} '
				bucket_values['colours'] = colours
				continue
			bucket_values[field] = bucket.get(f'{field}', '')
		bucket = BucketsDetails.objects.create(**bucket_values)
		print('b', bucket.id)

	# for bucket, image in zip(buckets, images):
	# 	bucket_colours = bucket.get('colours')
	# 	colours = ''
	# 	for colour in bucket_colours:
	# 		colours += f'{colour} '
	# 	BucketsDetails.objects.create(
	# 		order_id=new_order_model.id,
	# 		colours=colours,
	# 		rose_amount=bucket.get('rose_amount'),
	# 		packing=bucket.get('packing'),
	# 		rose_box=bucket.get('rose_box'),
	# 		price=bucket.get('price'),
	# 		image=image,
	# 	)



def update_order(order, order_model, buckets, images):
	for field in order:
		if field == 'given_date':
			date_format = "%H:%M %d/%m/%Y"
			setattr(order_model, field, datetime.strptime(order.get(f'{field}'), date_format))
			continue
		setattr(order_model, field, order.get(f'{field}', ''))
	order_model.save()

	buckets_model = BucketsDetails.objects.filter(order_id=order_model.id)
	for bucket, bucket_model in zip(buckets, buckets_model):
		for field in bucket:
			if field == 'colours':
				colours = ''
				for colour in bucket.get('colours'):
					colours += f'{colour} '
				setattr(bucket_model, field, colours)
				continue
			# elif field == 'image':
			# 	setattr(bucket_model, field, image)
			setattr(bucket_model, field, bucket.get(f'{field}', ''))
		bucket_model.save()



def search_order(search_value, search_status):
	order_date = search_date(search_value, search_status)
	order_number = search_number(search_value, search_status)
	if len(list(chain(order_date, order_number))) == 0:
		return []
	return list(chain(order_date, order_number))



def search_date(number, search_status):
	try:
		date = datetime.strptime(number, "%d/%m/%Y")
		if search_status != 'Все':
			result = Order.objects.annotate(
				given_day=Trunc('given_date', 'day', output_field=DateTimeField())).filter(
				given_day=date, order_status=search_status)
		else:
			result = Order.objects.annotate(
				given_day=Trunc('given_date', 'day', output_field=DateTimeField())).filter(
				given_day=date)
	except ValueError as exc:
		return []
	except Order.DoesNotExist as exc:
		return []
	except TypeError as exc:
		return []
	return result


def search_number(number, search_status):
	try:
		if search_status == 'Все':
			result = Order.objects.filter(number=number)
		else:
			result = Order.objects.filter(number=number, order_status=search_status)
	except ValueError as exc:
		return []
	except Order.DoesNotExist as exc:
		return []
	except TypeError as exc:
		return []
	return result
