import json
import environ
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from crm.models import (
	Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails, OrderStatus, OrderType)
from django.core.paginator import Paginator
from crm.orders import save_new_order, update_order, delete_order, search_order
from django.shortcuts import get_object_or_404


def is_ajax(request):
	return request.headers.get('x-requested-with') == 'XMLHttpRequest'


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
	search_value = request.GET.get('search_order', None)
	search_status = request.GET.get('search_status', None)

	orders = search_order(search_value, search_status)
	paginator = Paginator(orders, 10)
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)
	page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
	order_stats = OrderStatus.objects.all()

	context = {
		'search_status': search_status,
		'search_value': search_value,
		'page_obj': page_obj,
		'order_stats': order_stats,
	}

	return render(request, 'crm/orders.html', context=context)


@staff_member_required
def order_req(request, order_number):
	colours = RoseColour.objects.all()
	rose_amount = RoseAmount.objects.all()
	boxes = RoseBoxes.objects.all()
	rose_packing = RosePacking.objects.all()
	order_stats = OrderStatus.objects.all()
	order_types = OrderType.objects.all()
	order = get_object_or_404(Order, number=order_number)
	buckets = BucketsDetails.objects.filter(order_id=order.id)
	bucket_colours = [bucket.colours.split() for bucket in buckets]

	context = {
		'colours': colours,
		'rose_amounts': rose_amount,
		'boxes': boxes,
		'rose_packings': rose_packing,
		'order_stats': order_stats,
		'order_types': order_types,

		'order': order,
		'buckets': zip(buckets, bucket_colours),
		'bucket_colours': bucket_colours,
	}

	return render(request, 'crm/order.html', context=context)


@staff_member_required
def add_order(request):
	colours = RoseColour.objects.all()
	rose_amount = RoseAmount.objects.all()
	boxes = RoseBoxes.objects.all()
	rose_packing = RosePacking.objects.all()
	order_stats = OrderStatus.objects.all()
	order_types = OrderType.objects.all()

	try:
		last_order_num = Order.objects.last().number + 1
	except AttributeError:
		last_order_num = None

	context = {
		'colours': colours,
		'rose_amounts': rose_amount,
		'boxes': boxes,
		'rose_packings': rose_packing,
		'last_order_num': last_order_num,
		'order_stats': order_stats,
		'order_types': order_types,
	}

	return render(request, 'crm/add_order.html', context=context)


@staff_member_required
def save_order(request):
	order = json.loads(request.POST.get('order'))
	buckets = json.loads(request.POST.get('buckets'))
	print(request.FILES)
	user = request.user
	images = [request.FILES.get(image) for image in request.FILES]

	# try:
	# 	order_model = Order.objects.get(number=order.get('number', 'None'))
	# 	update_order(order, order_model, buckets, images)
	# except Order.DoesNotExist:
	# 	save_new_order(order, buckets, user, images)

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
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	box_name = request.POST.get('box_name')
	try:
		box = RoseBoxes.objects.create(box=box_name, status=True)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)

	return JsonResponse({'response': 'good', 'box_id': box.id})


@staff_member_required
def status_box(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	box_status = request.POST.get('box_status')
	box_id = request.POST.get('box_id')
	try:
		box = RoseBoxes.objects.get(id=box_id)
		box.status = box_status
		box.save()
	except RoseBoxes.DoesNotExist as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'})


@staff_member_required
def delete_box(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
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
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	box_name = request.POST.get('box_name')
	box_id = request.POST.get('box_id')
	try:
		box = RoseBoxes.objects.get(id=box_id)
		box.box = box_name
		box.save()
	except RoseBoxes.DoesNotExist as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'})


# endregion

# region packings

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
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	packing_name = request.POST.get('packing_name')
	try:
		packing = RosePacking.objects.create(packing=packing_name, status=True)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good', 'packing_id': packing.id}, status=200)


@staff_member_required
def status_packing(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	packing_status = request.POST.get('packing_status')
	packing_id = request.POST.get('packing_id')
	try:
		packing = RosePacking.objects.get(id=packing_id)
		packing.status = packing_status
		packing.save()
	except RosePacking.DoesNotExist as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'})


@staff_member_required
def delete_packing(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	try:
		packing_id = request.POST.get('packing_id')
		RosePacking.objects.get(id=packing_id).delete()
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)

	return JsonResponse({'response': 'good'}, status=200)


@staff_member_required
def update_packing(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	packing_id = request.POST.get('packing_id')
	packing_name = request.POST.get('packing_name')
	try:
		packing = RosePacking.objects.get(id=packing_id)
		packing.packing = packing_name
		packing.save()
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)
	return JsonResponse({'response': 'good'})


# endregion


@staff_member_required
def rose_colours(request):
	colours = RoseColour.objects.all()
	context = {'colours': colours}
	return render(request, 'crm/colours.html', context=context)


@staff_member_required
def add_colour(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	try:
		colour = RoseColour.objects.create(colour=request.POST.get('colour'), status=True)
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)

	return JsonResponse({'response': 'good', 'colour_id': colour.id}, status=200)


@staff_member_required
def delete_colour(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	try:
		colour_id = request.POST.get('colour_id')
		RoseColour.objects.get(id=colour_id).delete()
	except Exception as exc:
		return JsonResponse({'error': exc}, status=500)
	return JsonResponse({'response': 'good'})


@staff_member_required
def update_colour(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	colour_id = request.POST.get('colour_id')
	colour = request.POST.get('colour')
	print(colour)
	try:
		colour_obj = RoseColour.objects.get(id=colour_id)
		colour_obj.colour = colour
		colour_obj.save()
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	return JsonResponse({'response': 'good'})


@staff_member_required
def status_colour(request):
	if not is_ajax(request):
		return JsonResponse({'error': 'request in not ajax'}, status=400)
	colour_status = request.POST.get('colour_status')
	colour_id = request.POST.get('colour_id')
	try:
		colour = RoseColour.objects.get(id=colour_id)
		colour.status = colour_status
		colour.save()
	except RoseColour.DoesNotExist as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except TypeError as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)
	except Exception as exc:
		return JsonResponse({'error': f'{exc}'}, status=500)

	return JsonResponse({'response': 'good'})


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
