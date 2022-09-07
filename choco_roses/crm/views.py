import json
import environ
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from crm.models import (
	Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails, OrderStatus)
from django.core.paginator import Paginator
from crm.orders import save_new_order, update_order, delete_order, search_order
from django.core.files import File

def get_environ():
	env = environ.Env()
	environ.Env.read_env()
	return env


@staff_member_required
def index(request):
	orders_list = Order.objects.order_by('-given_date')
	nearest_orders = [order for order in orders_list]

	order_stats = OrderStatus.objects.all()
	data = {order_status: Order.objects.filter(order_status=order_status) for order_status in order_stats}
	context = {
		'nearest_orders': nearest_orders,
		'data': data
	}
	return render(request, 'crm/index.html', context=context)


# region orders
@staff_member_required
def orders_req(request):

	number = request.GET.get('search_order', None)
	search_result = search_order(number)

	orders = Order.objects.all()
	paginator = Paginator(orders, 10)
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)
	page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

	context = {
		'page_obj': page_obj,
		'search_order': search_result,
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

	try:
		last_order_num = Order.objects.last().number + 1
	except AttributeError:
		last_order_num = None

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

	order = json.loads(request.POST.get('order'))
	buckets = json.loads(request.POST.get('buckets'))
	user = request.user
	images = [request.FILES.get(image) for image in request.FILES]

	try:
		order_model = Order.objects.get(number=order.get('number', 'None'))
		update_order(order, order_model, buckets, images)
	except Order.DoesNotExist:
		save_new_order(order, buckets, user, images)

	return JsonResponse({'response': 'good'})


@staff_member_required
def delete_order(request):
	order_number = request.POST.get('order_number')
	try:
		order = Order.objects.get(number=order_number)
		order.delete()
	except Order.DoesNotExist as exc:
		return JsonResponse({'error': exc}, status=500)
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)
	return JsonResponse({'response': 'good'}, status=200)


# endregion


# region boxes

@staff_member_required
def rose_boxes(request):
	try:
		boxes = RoseBoxes.objects.all()
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)
	context = {
		'boxes': boxes
	}
	return render(request, 'crm/rose-boxes.html', context=context)


@staff_member_required
def add_box(request):
	box_name = request.POST.get('box_name')
	try:
		box = RoseBoxes.objects.create(rose_box=box_name)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)

	return JsonResponse({'response': 'good', 'box_id': box.id})


@staff_member_required
def delete_box(request):
	box_id = request.POST.get('box_id')
	try:
		RoseBoxes.objects.get(id=box_id).delete()
	except RoseBoxes.DoesNotExist as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'})


@staff_member_required
def update_box(request):
	box_name = request.POST.get('box_name')
	box_id = request.POST.get('box_id')
	try:
		box = RoseBoxes.objects.get(id=box_id)
		box.rose_box = box_name
		box.save()
	except RoseBoxes.DoesNotExist as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'})

# endregion


@staff_member_required
def rose_packings(request):
	try:
		packings = RosePacking.objects.all()
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	context = {
		'packings': packings
	}
	return render(request, 'crm/rose-packings.html', context=context)


@staff_member_required
def add_packing(request):
	packing_name = request.POST.get('packing_name')
	try:
		packing = RosePacking.objects.create(rose_packing=packing_name)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good', 'packing_id': packing.id}, status=200)


@staff_member_required
def delete_packing(request):
	packing_id = request.POST.get('packing_id')
	try:
		RosePacking.objects.get(id=packing_id).delete()
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'}, status=200)


@staff_member_required
def update_packing(request):
	packing_id = request.POST.get('packing_id')
	packing_name = request.POST.get('packing_name')
	try:
		packing = RosePacking.objects.get(id=packing_id)
		packing.rose_packing = packing_name
		packing.save()
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)
	return JsonResponse({'response': 'good'})


@staff_member_required
def add_rose_colour(request):
	pass


@staff_member_required
def delete_rose_colour(request):
	pass


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
def products(request):
	return render(request, 'crm/products.html')


@staff_member_required
def settings(request):
	return render(request, 'crm/settings.html')


@staff_member_required
def todo(request):
	return render(request, 'crm/todo.html')
