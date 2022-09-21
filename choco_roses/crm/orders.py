from datetime import datetime
from crm.models import Order, BucketsDetails
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from itertools import chain



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


	for bucket in buckets:
		bucket_values = {'order_id': new_order_model.id}
		for field in bucket:
			if field == 'id':
				continue
			if field == 'colours':
				bucket_colours = bucket.get('colours')
				colours = ''
				for colour in bucket_colours:
					colours += f'{colour} '
				bucket_values['colours'] = colours
				continue
			elif field == 'image':
				image = str(bucket.get('id'))
				bucket_values[field] = image
			bucket_values[field] = bucket.get(f'{field}', '')
		BucketsDetails.objects.create(**bucket_values)


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
			elif field == 'image':
				image = str(bucket.get('id'))
				setattr(bucket_model, field, image)
			setattr(bucket_model, field, bucket.get(f'{field}', ''))
		bucket_model.save()



def search_order(search_value, search_status):
	if search_value and search_status != 'Все' or search_value and search_status == 'Все':
		order_date = search_date(search_value, search_status)
		order_number = search_number(search_value, search_status)
		# if len(list(chain(order_date, order_number))) == 0:
		# 	return []
		orders = list(chain(order_date, order_number))
		return orders
	elif search_status and search_status != 'Все':
		orders = Order.objects.filter(order_status=search_status)
		return orders
	else:
		orders = Order.objects.all().order_by('-number')
		return orders


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
	except Exception as exc:
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
	except Exception as exc:
		return []
	return result
