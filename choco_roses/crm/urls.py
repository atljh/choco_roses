from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import validators

urlpatterns = [
	path('', views.index, name='index'),
	path('orders/', views.orders_req, name='orders'),
	path('order/<int:order_number>/', views.order_req, name='order'),
	path('add_order/', views.add_order, name='add-order'),
	path('delete_order/', views.delete_order, name='delete-order'),
	path('save_order/', views.save_order, name='save-order'),
	path('save_order/', views.save_order, name='save-order'),

	path('boxes/', views.rose_boxes, name='boxes'),
	path('add_box/', views.add_box, name='add-box'),
	path('delete_box/', views.delete_box, name='add-boxes'),
	path('update_box/', views.update_box, name='add-boxes'),
	path('box_status/', views.status_box, name='status-box'),
	path('packings/', views.rose_packings, name='packings'),
	path('add_packing/', views.add_packing, name='add-packing'),
	path('packing_status/', views.status_packing, name='status-packing'),
	path('delete_packing/', views.delete_packing, name='delete-packing'),
	path('update_packing/', views.update_packing, name='update-packing'),
	path('calendar/', views.calendar, name='calendar'),
	path('products/', views.products, name='products'),
	path('settings/', views.settings, name='settings'),
	path('todo/', views.todo, name='todo'),

	# path('clients/', views.clients_req, name='clients'),
	# path('clients/<int:client_id>/', views.client_req, name='client'),
	# path('add_client/', views.add_client, name='add-client'),

	path('validate_number/', validators.validate_number, name='validate-number'),
	path('validate_name/', validators.validate_name, name='validate-name'),
	path('validate_address/', validators.validate_address, name='validate-address'),
	path('validate_phone/', validators.validate_phone, name='validate-phone'),
	path('validate_instagram/', validators.validate_instagram, name='validate-instagram'),
	path('validate_delivery_data/', validators.validate_delivery_data, name='validate-delivery-data'),
	path('validate_pickup_data/', validators.validate_pickup_data, name='validate-pickup-data'),
	path('validate_payment/', validators.validate_payment, name='validate-payment'),
	path('validate_from_where/', validators.validate_from_where, name='validate-from-where'),
	path('validate_description/', validators.validate_description, name='validate-description'),
	path('validate_total_price/', validators.validate_total_price, name='validate-total_price'),
	path('validate_price/', validators.validate_price, name='validate-price'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
