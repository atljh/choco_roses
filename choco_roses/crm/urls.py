from . import views
from .orders import views as order_views
from . import products
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .components import components
from . import validators

urlpatterns = [
	path('', views.index, name='index'),
	path('orders/', order_views.orders_req, name='orders'),
	path('order/<int:order_number>/', order_views.order_req, name='order'),
	path('add_order/', order_views.add_order, name='add-order'),
	path('delete_order/', order_views.delete_order, name='delete-order'),
	path('save_order/', order_views.save_order, name='save-order'),

	path('boxes/', components.rose_boxes, name='boxes'),
	path('add_box/', components.add_box, name='add-box'),
	path('delete_box/', components.delete_box, name='add-boxes'),
	path('update_box/', components.update_box, name='update-boxes'),
	path('box_status/', components.status_box, name='status-box'),

	path('packings/', components.rose_packings, name='packings'),
	path('add_packing/', components.add_packing, name='add-packing'),
	path('packing_status/', components.status_packing, name='status-packing'),
	path('delete_packing/', components.delete_packing, name='delete-packing'),
	path('update_packing/', components.update_packing, name='update-packing'),

	path('colours/', components.rose_colours, name='rose-colours'),
	path('add_colour/', components.add_colour, name='add-colour'),
	path('delete_colour/', components.delete_colour, name='add-colour'),
	path('update_colour/', components.update_colour, name='add-colour'),
	path('colour_status/', components.status_colour, name='status-colour'),

	path('products/', products.products, name='products'),
	path('product/', products.product, name='product'),
	path('add_product/', products.add_product, name='add-product'),
	path('save_product/', products.save_product_view, name='save-product'),
	path('update_product/', products.update_product, name='update-product'),
	path('add_products/', products.delete_product, name='delete'),

	path('calendar/', views.calendar, name='calendar'),
	path('settings/', views.settings, name='settings'),
	path('todo/', views.todo, name='todo'),

	# path('clients/', views.clients_req, name='clients'),
	# path('clients/<int:client_id>/', views.client_req, name='client'),
	# path('add_client/', views.add_client, name='add-client'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
