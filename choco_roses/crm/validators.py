from django.contrib.auth.models import User
from django.http import JsonResponse
import json


def validate_number(request):
	number = request.GET.get('number')

	def validate(number):
		if not number.isdigit():
			return False
		if int(number) < 0 or len(str(number)) > 50:
			return False
		return True

	data = {
		'result': validate(number)
	}

	return JsonResponse(data)


def validate_name(request):
	name = request.GET.get('name_surname')

	def validate(name: str):
		if not name.isalpha():
			return False
		if 1 > len(name) > 50:
			return False
		return True

	data = {
		'result': validate(name)
	}

	return JsonResponse(data)


# Address can be empty in case of pickup

def validate_address(request):
	address = request.GET.get('address')

	def validate(address):
		if address == '':
			return True
		if len(address) > 50:
			return False
		return True

	data = {
		'result': validate(address)
	}

	return JsonResponse(data)


def validate_phone(request):
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


def validate_instagram(request):
	instagram = request.GET.get('instagram')

	def validate(instagram):
		if instagram == '':
			return True
		if len(instagram) > 50:
			return False
		return True

	data = {
		'result': validate(instagram)
	}

	return JsonResponse(data)

# TODO: create more validatos
