from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import Product, Order



def index(request):
    print(Product.objects.all())
    # create_product = Product.objects.create(name=name, price=price, color=color, amount=amount, descriprion)
    # create_amount = RoseAmount.objects.create(amount=amount)
    # print(request.user.is_superuser)

    return render(request, 'crm/index.html')


def orders_req(request):
    orders = Order.objects.all()
    return render(request, 'crm/orders.html', {'orders': orders})


def order_req(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'crm/order.html', {'order': order})


def clients_req(request):
    return render(request, 'crm/clients.html')


def client_req(request):
    return render(request, 'crm/client.html')


def add_order(request):
    return render(request, 'crm/add_order.html')


def add_client(request):
    return render(request, 'crm/add_client.html')



# class AccountAPIView(generics.ListCreateAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#
#
# class ActivityAPIView(generics.ListCreateAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#
#
# class ActivityStatusAPIView(generics.ListCreateAPIView):
#     queryset = ActivityStatus.objects.all()
#     serializer_class = ActivitySerializer
#
#
# class ContactAPIView(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactStatusAPIView(generics.ListCreateAPIView):
#     queryset = ContactStatus.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactSourceAPIView(generics.ListCreateAPIView):
#     queryset = ContactSource.objects.all()
#     serializer_class = ContactSourceSerializer
