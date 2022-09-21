from .models import RosePacking, RoseAmount, RoseBoxes, RoseColour
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .views import is_ajax
from django.shortcuts import render


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


# region rose colours

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


# endregion
