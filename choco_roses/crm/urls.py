from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.orders_req, name='orders'),
    path('orders/', views.orders_req, name='orders'),
    path('order/<int:order_id>/', views.order_req, name='order'),
    path('clients/', views.clients_req, name='clients'),
    path('clients/<int:client_id>/', views.client_req, name='client'),
    path('add_order/', views.add_order, name='add-order'),
    path('add_client/', views.add_client, name='add-client'),
]
