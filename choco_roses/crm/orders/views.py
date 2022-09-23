import json
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render
from crm.views import is_ajax
from crm.models import (
	Order, RoseColour, RoseAmount, RoseBox, RosePacking, BucketsDetails, OrderStatus, OrderType)
from django.core.paginator import Paginator
from .orders import save_new_order, update_order, search_order
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


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
	boxes = RoseBox.objects.all()
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
	boxes = RoseBox.objects.all()
	rose_packings = RosePacking.objects.all()
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
		'rose_packings': rose_packings,
		'last_order_num': last_order_num,
		'order_stats': order_stats,
		'order_types': order_types,
	}

	return render(request, 'crm/add_order.html', context=context)


@staff_member_required
def save_order(request):
    if not is_ajax(request):
        return HttpResponse('Request is not ajax', status=400)
    order = json.loads(request.POST.get('order'))
    buckets = json.loads(request.POST.get('buckets'))
    user = request.user
    images = request.FILES
    print(buckets)

    try:
        order_model = Order.objects.get(number=order.get('number', 'None'))
        update_order(order, order_model, buckets, images)
    except Order.DoesNotExist:
        try:
            save_new_order(order, buckets, user, images)
        except Exception as exc:
            return JsonResponse({'error': f'{exc}'}, status=500)
    except Exception as exc:
        return JsonResponse({'response': f'{exc}'}, status=500)
    return JsonResponse({'response': 'good'}, status=200)


@staff_member_required
def delete_order(request):
    if not is_ajax(request):
        return HttpResponse('Request is not ajax', status=400)
    order_number = request.POST.get('order_number')
    try:
        order = Order.objects.get(number=order_number)
        order.delete()
    except Order.DoesNotExist as exc:
        return JsonResponse({'error': exc}, status=500)
    except Exception as exc:
        return JsonResponse({'error': exc}, status=500)
    return JsonResponse({'response': 'good'}, status=200)
