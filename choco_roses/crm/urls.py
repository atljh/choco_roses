from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.orders_req, name='orders'),
    path('order/<int:order_id>/', views.order_req, name='order'),
    path('add_order/', views.add_order, name='add-order'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit-order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete-order'),
    path('save_bucket/', views.save_order, name='save-order'),
    path('clients/', views.clients_req, name='clients'),
    path('clients/<int:client_id>/', views.client_req, name='client'),
    path('add_client/', views.add_client, name='add-client'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)