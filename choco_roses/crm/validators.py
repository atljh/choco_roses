from django.contrib.auth.models import User
from django.http import JsonResponse
import json


def validate_number(request) -> JsonResponse:
	number = request.GET.get('number')

	def validate(number):
		if not number.isdigit():
			return False
		if int(number) < 0 or len(str(number)) > 50 or len(str(number)) < 1:
			return False
		return True

	data = {
		'result': validate(number)
	}

	return JsonResponse(data)


def validate_name(request) -> JsonResponse:
	name_surname = request.GET.get('name_surname')

	def validate(name_surname: str):
		if len(name_surname) > 100 or len(name_surname) < 1:
			return False
		return True

	data = {
		'result': validate(name_surname)
	}

	return JsonResponse(data)


# Address can be empty in case of pickup

def validate_address(request) -> JsonResponse:
	address = request.GET.get('address')

	def validate(address):
		if address == '':
			return True
		if len(address) > 100:
			return False
		return True

	data = {
		'result': validate(address)
	}

	return JsonResponse(data)


def validate_phone(request) -> JsonResponse:
	phone = request.GET.get('phone')

	def validate(phone):
		if phone == '':
			return True
		if not phone.isdigit():
			return False
		if int(phone) < 0 or len(str(phone)) > 50:
			return False
		return True

	data = {
		'result': validate(phone)
	}

	return JsonResponse(data)


def validate_instagram(request) -> JsonResponse:
	instagram = request.GET.get('instagram')

	def validate(instagram):
		if instagram == '':
			return True
		if len(instagram) > 100:
			return False
		return True

	data = {
		'result': validate(instagram)
	}

	return JsonResponse(data)


def validate_delivery_data(request) -> JsonResponse:
	delivery_data = request.GET.get('delivery_data')

	def validate(delivery_data):
		if delivery_data == '':
			return True
		if len(delivery_data) > 100:
			return False
		return True

	data = {
		'result': validate(delivery_data)
	}

	return JsonResponse(data)


def validate_pickup_data(request) -> JsonResponse:
	pickup_data = request.GET.get('pickup_data')

	def validate(pickup_data):
		if pickup_data == '':
			return True
		if len(pickup_data) > 100:
			return False
		return True

	data = {
		'result': validate(pickup_data)
	}

	return JsonResponse(data)


def validate_payment(request) -> JsonResponse:
	payment = request.GET.get('payment')

	def validate(payment):
		if payment == '':
			return True
		if len(payment) > 50:
			return False
		return True

	data = {
		'result': validate(payment)
	}

	return JsonResponse(data)


def validate_from_where(request) -> JsonResponse:
	from_where = request.GET.get('from_where')

	def validate(from_where):
		if from_where == '':
			return True
		if len(from_where) > 50:
			return False
		return True

	data = {
		'result': validate(from_where)
	}

	return JsonResponse(data)


def validate_description(request) -> JsonResponse:
	description = request.GET.get('description')

	def validate(description):
		if description == '':
			return True
		if len(description) > 400:
			return False
		return True

	data = {
		'result': validate(description)
	}

	return JsonResponse(data)



def validate_total_price(request) -> JsonResponse:
	total_price = request.GET.get('total_price')

	def validate(total_price):
		if not total_price.isdigit():
			return False
		if int(total_price) < 0 or len(str(total_price)) > 50 or len(str(total_price)) < 1:
			return False
		return True

	data = {
		'result': validate(total_price)
	}

	return JsonResponse(data)



def validate_price(request) -> JsonResponse:
	price = request.GET.get('price')

	def validate(price):
		if not price.isdigit():
			return False
		if int(price) < 0 or len(str(price)) > 50 or len(str(price)) < 1:
			return False
		return True

	data = {
		'result': validate(price)
	}

	return JsonResponse(data)


