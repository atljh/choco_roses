import json
from crm.models import Product, RoseAmount, RoseBox, RoseColour, RosePacking
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse
from .views import is_ajax
from django.shortcuts import render
from django.shortcuts import get_object_or_404




@staff_member_required
def products(request):
    products = Product.objects.all()
    context = {'products': products}
    
    return render(request, 'crm/products.html', context=context)


@staff_member_required
def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'crm/product.html', context=context)


@staff_member_required
def add_product(request):
    colours = RoseColour.objects.all()
    boxes = RoseBox.objects.all()
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
def save_product_view(request):
    if not is_ajax(request):
        return HttpResponse('Request is not ajax', status=400)
    product = json.loads(request.POST.get('product'))
    image = request.FILES
    try:
        save_product(product, image)
    except Exception as exc:
        return JsonResponse({'error': f'{exc}'}, status=500)
    return JsonResponse({'response': 'good'}, status=200)


@staff_member_required
def delete_product(request):
    if not is_ajax(request):
        return HttpResponse({'Request is not ajax'}, status=400)
    product_id = request.GET.get('product_id')
    Product.objects.get(id=product_id).delete()
    return JsonResponse({'response': 'good'}, status=200)


@staff_member_required
def update_product(request):
    if not is_ajax(request):
        return JsonResponse({'error': 'Request is not ajax'}, status=400)
    return HttpResponse({'response': 'good'}, status=200)




def save_product(product, image):
    product_values = {}
    for field in product:
        product_values[field] = product.get(f'{field}', '')
    product_values['image'] = image.get('image')
    try:
        product_model = Product.objects.create(**product_values)
        return product_model.id
    except Exception as exc:
        return exc
