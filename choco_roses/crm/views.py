from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, auth
from main.models import (
    Product, Order, RoseColour, RoseAmount, RoseBoxes, RosePacking, BucketsDetails, BucketsColours)
import environ
from django.contrib.admin.views.decorators import staff_member_required

env = environ.Env()
environ.Env.read_env()


@staff_member_required
def index(request):
    # create_product = Product.objects.create(name=name, price=price, color=color, amount=amount, descriprion)
    # create_amount = RoseAmount.objects.create(amount=amount)
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
    buckets = BucketsDetails.objects.get(order_id=order.id)
    buckets_colours = BucketsColours.objects.get(bucket_id=buckets.id)
    colours = RoseColour.objects.all()
    rose_amount = RoseAmount.objects.all()
    boxes = RoseBoxes.objects.all()
    rose_packing = RosePacking.objects.all()

    print(order.id)


    context = {
        'colours': colours,
        'rose_amount': rose_amount,
        'boxes': boxes,
        'rose_packing': rose_packing,
        'order': order,
        'buckets': buckets,
        'buckets_colours': buckets_colours
    }
    return render(request, 'crm/order-edit.html', context=context)


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

    return render(request, 'crm/test.html', context=context)



@staff_member_required
def save_order(request):

    # Order details
    bucket = 0
    total_price = request.POST.get('total_price', 'None')
    name_surname = request.POST.get('name_surname', 'None')
    instagram = request.POST.get('instagram', 'None')
    from_where = request.POST.get('from_where', 'None')
    address = request.POST.get('address', 'None')
    phone = request.POST.get('phone', 'None')
    order_type = request.POST.get('order_type', 'None')
    order_status = request.POST.get('order_status', 'None')
    anonymous = request.POST.get('anonymous', 'False')
    first_order = request.POST.get('first_order', 'False')
    delivery_data = request.POST.get('delivery_data', 'None')
    pickup_data = request.POST.get('pickup_data', 'None')
    payment = request.POST.get('payment', 'None')
    description = request.POST.get('description', 'None')




    # Save Order model
    # order = Order.objects.create(
    #         bucket=bucket,
    #         total_price=total_price,
    #         name_surname=name_surname,
    #         instagram=instagram,
    #         from_where=from_where,
    #         address=address,
    #         phone=phone,
    #         order_type=order_type,
    #         order_status=order_status,
    #         anonymous=bool(anonymous),
    #         first_order=bool(first_order),
    #         delivery_data=delivery_data,
    #         pickup_data=pickup_data,
    #         payment=payment,
    #         created_by=str(request.user),
    #         description=description
    #     )

    # Bucket details
    # order_id = order.id
    colour1 = request.POST.get('colour1', 'None')
    colour2 = request.POST.get('colour2', 'None')
    colour3 = request.POST.get('colour3', 'None')
    colour4 = request.POST.get('colour4', 'None')
    colour5 = request.POST.get('colour5', 'None')
    colour6 = request.POST.get('colour6', 'None')
    colour7 = request.POST.get('colour7', 'None')
    rose_amount = request.POST.get('rose_amount', 'None')
    packing = request.POST.get('packing', 'None')
    rose_box = request.POST.get('box', 'None')
    price = request.POST.get('price', 'None')

    # Save BucketDetails model
    # bucket = BucketsDetails.objects.create(
    #     order_id=order_id,
    #     colours=0,
    #     rose_amount=rose_amount,
    #     packing=packing,
    #     rose_box=rose_box,
    #     price=price
    # )


    # Save BucketsColours model
    # colours = BucketsColours.objects.create(
    #     bucket_id=bucket.id,
    #     colour1=colour1,
    #     colour2=colour2,
    #     colour3=colour3,
    #     colour4=colour4,
    #     colour5=colour5,
    #     colour6=colour6,
    #     colour7=colour7
    # )


    # bucket.colours = colours.id
    # bucket.save()
    # order.bucket = bucket.id
    # order.save()


    price = request.POST.get('colour1', 'None')
    print(price)

    return redirect('/crm/add_order/')




@staff_member_required
def save_bucket(request):
    order_id = 0
    colour1 = request.POST.get('colour1', 'None')
    colour2 = request.POST.get('colour2', 'None')
    colour3 = request.POST.get('colour3', 'None')
    colour4 = request.POST.get('colour4', 'None')
    colour5 = request.POST.get('colour5', 'None')
    colour6 = request.POST.get('colour6', 'None')
    colour7 = request.POST.get('colour7', 'None')
    rose_amount = request.POST.get('rose_amount', 'None')
    packing = request.POST.get('packing', 'None')
    rose_box = request.POST.get('box', 'None')
    price = request.POST.get('price', 'None')


    # Save BucketDetails model
    # bucket = BucketsDetails.objects.create(
    #     order_id=order_id,
    #     colours=0,
    #     rose_amount=rose_amount,
    #     packing=packing,
    #     rose_box=rose_box,
    #     price=price
    # )



    return redirect('/crm/add_order/')



@staff_member_required
def edit_order(request, order_id):

    order = Order.objects.get(id=order_id)
    buckets = BucketsDetails.objects.get(order_id=order.id)
    buckets_colours = BucketsColours.objects.get(bucket_id=buckets.id)


    total_price = request.POST.get('total_price', 'None')
    name_surname = request.POST.get('name_surname', 'None')
    instagram = request.POST.get('instagram', 'None')
    from_where = request.POST.get('from_where', 'None')
    address = request.POST.get('address', 'None')
    phone = request.POST.get('phone', 'None')
    order_type = request.POST.get('order_type', 'None')
    order_status = request.POST.get('order_status', 'None')
    anonymous = request.POST.get('anonymous', 'False')
    first_order = request.POST.get('first_order', 'False')
    delivery_data = request.POST.get('delivery_data', 'None')
    pickup_data = request.POST.get('pickup_data', 'None')
    payment = request.POST.get('payment', 'None')
    description = request.POST.get('description', 'None')


    # Save edited Order model
    order.total_price = total_price
    order.name_surname = name_surname
    order.instagram = instagram
    order.from_where = from_where
    order.address = address
    order.phone =phone
    order.order_type = order_type
    order.order_status = order_status
    order.anonymous = anonymous
    order.first_order = first_order
    order.delivery_data = delivery_data
    order.pickup_data = pickup_data
    order.payment = payment
    order.description = description

    order.save()


    colour1 = request.POST.get('colour1', 'None')
    colour2 = request.POST.get('colour2', 'None')
    colour3 = request.POST.get('colour3', 'None')
    colour4 = request.POST.get('colour4', 'None')
    colour5 = request.POST.get('colour5', 'None')
    colour6 = request.POST.get('colour6', 'None')
    colour7 = request.POST.get('colour7', 'None')
    rose_amount = request.POST.get('rose_amount', 'None')
    packing = request.POST.get('packing', 'None')
    rose_box = request.POST.get('box', 'None')
    price = request.POST.get('price', 'None')


    # Save BucketDetails model
    buckets.rose_amount = rose_amount
    buckets.packing = packing
    buckets.rose_box = rose_box
    buckets.price = price

    buckets.save()


    # Save BucketsColours model
    buckets_colours.colour1 = colour1
    buckets_colours.colour2 = colour2
    buckets_colours.colour3 = colour3
    buckets_colours.colour4 = colour4
    buckets_colours.colour5 = colour5
    buckets_colours.colour6 = colour6
    buckets_colours.colour7 = colour7

    buckets_colours.save()

    return redirect(f'/crm/order/{order_id}/')


@staff_member_required
def delete_order(request, order_id):
    pass


def add_client(request):
    return render(request, 'add_client.html')
