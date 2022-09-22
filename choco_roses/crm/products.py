from .models import Product, RoseAmount, RoseBoxes, RoseColour, RosePacking
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .views import is_ajax
from django.shortcuts import render



@staff_member_required
def products(request):
	return render(request, 'crm/products.html')


@staff_member_required
def product(request, product_id):
    product = Product.objects.get(id=request.GET.get('product_id'))
    context = {'product': product}
    return render(request, 'crm/product.html', context=context)


@staff_member_required
def add_product(request):
    colours = RoseColour.objects.all()
    boxes = RoseBoxes.objects.all()
    packings = RosePacking.objects.all()
    rose_amounts = RoseAmount.objects.all()

    context = {
        'colours': colours,
        'boxes': boxes,
        'rose_packings': packings,
        'rose_amounts': rose_amounts
               }
    return render(request, 'crm/add_product.html', context=context)


@staff_member_required
def save_product(request):
    if not is_ajax(request):
        return JsonResponse({'error': 'Request is not ajax'}, status=400)
    product = request.POST.get('product')
    print(product)
    return JsonResponse({'response': 'succes'}, status=200)
    try:
        # product = Product.objects.get(id=product)
        ...
    except Product.DoesNotExist:
        # product = Product(id=product)
        ...

@staff_member_required
def delete_product(request):
    if not is_ajax(request):
        return JsonResponse({'error': 'Request is not ajax'}, status=400)
    return JsonResponse({'response': 'good'}, status=200)


@staff_member_required
def update_product(request):
    if not is_ajax(request):
        return JsonResponse({'error': 'Request is not ajax'}, status=400)
    return JsonResponse({'response': 'good'}, status=200)
