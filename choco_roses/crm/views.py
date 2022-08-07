from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, auth
from main.models import (
    Product, Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails)
import environ
from django.contrib.admin.views.decorators import staff_member_required

env = environ.Env()
environ.Env.read_env()


@staff_member_required
def index(request):
    # create_product = Product.objects.create(name=name, price=price, color=color, amount=amount, descriprion)
    # create_amount = RoseAmount.objects.create(amount=amount)
    orders = Order.objects.get(bucket=11)
    print(orders)
    return render(request, 'crm/index.html')


@staff_member_required
def orders_req(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }

    return render(request, 'crm/orders.html', context=context)


@staff_member_required
def order_req(request, order_id):
    order = Order.objects.get(id=order_id)
    buckets = Order.objects.get(bucket=order.bucket)
    context = {
        'order': order,
        'buckets': buckets
    }

    return render(request, 'order.html', context=context)


@staff_member_required
def clients_req(request):
    return render(request, 'clients.html')


@staff_member_required
def client_req(request):
    return render(request, 'client.html')


@staff_member_required
def add_order(request):
    colours = RoseColour.objects.all()
    rose_amount = RoseAmount.objects.all()
    boxes = RoseBoxes.objects.all()
    rose_packing = RosePacking.objects.all()
    context = {
        'colours': colours,
        'rose_amount': rose_amount,
        'boxes': boxes,
        'rose_packing': rose_packing
    }

    buckets_amount = 0
    buckets_list = []



    return render(request, 'crm/add_order.html', context=context)



@staff_member_required
def save_order(request):

    # Order details
    bucket = 0
    total_price = request.POST.get('total_price', 'No')
    name_surname = request.POST.get('name_surname', 'No')
    instagram = request.POST.get('instagram', 'No')
    from_where = request.POST.get('from_where', 'No')
    address = request.POST.get('address', 'No')
    phone = request.POST.get('phone', 'No')
    order_type = request.POST.get('order-type', 'No')
    anonymous = request.POST.get('anonymous', 'False')
    first_order = request.POST.get('first_order', 'False')
    delivery_data = request.POST.get('delivery_data', 'No')
    pickup_data = request.POST.get('pickup_data', 'No')
    payment = request.POST.get('payment', 'No')
    description = request.POST.get('description', 'No')




    # Save Order model
    order = Order.objects.create(
            bucket=bucket,
            total_price=total_price,
            name_surname=name_surname,
            instagram=instagram,
            from_where=from_where,
            address=address,
            phone=phone,
            order_type=order_type,
            anonymous=bool(anonymous),
            first_order=bool(first_order),
            delivery_data=delivery_data,
            pickup_data=pickup_data,
            payment=payment,
            created_by=str(request.user),
            description=description
        )

    # Bucket details
    order_id = order.id
    colour1 = request.POST.get('colour1', 'No')
    colour2 = request.POST.get('colour2', 'No')
    colour3 = request.POST.get('colour3', 'No')
    colour4 = request.POST.get('colour4', 'No')
    rose_amount = request.POST.get('rose_amount', 'No')
    packing = request.POST.get('packing', 'No')
    rose_box = request.POST.get('box', 'No')
    price = request.POST.get('price', 'No')

    # Save BucketDetails model
    bucket = BucketsDetails.objects.create(
        order_id=order_id,
        colour1=colour1,
        colour2=colour2,
        colour3=colour3,
        colour4=colour4,
        rose_amount=rose_amount,
        packing=packing,
        rose_box=rose_box,
        price=price
    )

    print(order.bucket)
    order.bucket = bucket.id
    order.save()
    print(order.bucket)

    return redirect('/crm/add_order')



@staff_member_required
def edit_order(request, order_id):
    pass


@staff_member_required
def delete_order(request, order_id):
    pass


def add_client(request):
    return render(request, 'add_client.html')
