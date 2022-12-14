from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator



class Client(models.Model):
	name = models.CharField(max_length=240)
	phone = models.CharField(max_length=20, null=True)
	instagram = models.CharField(max_length=100, null=True)
	from_where = models.CharField(max_length=100, null=True)
	address = models.CharField(max_length=300, null=True)
	email = models.EmailField(max_length=240, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('crm:detail-client', kwargs={'pk': self.pk})


class Product(models.Model):
	name = models.CharField(max_length=100)
	colours = models.CharField(max_length=150, blank=True, null=False)
	rose_amount = models.IntegerField(
		validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	packing = models.CharField(max_length=100, blank=True, null=True)
	rose_box = models.CharField(max_length=100, blank=True, null=True)
	price = models.IntegerField(
		default=0, validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	image = models.ImageField(upload_to='products/', null=True)
	description = models.CharField(
		max_length=250, default='', blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in=ids)

	@staticmethod
	def get_all_products():
		return Product.objects.all()

	def __str__(self):
		return self.name
	
	class Mera:
		ordering = ['date_created']


class RoseBox(models.Model):
	box = models.CharField(max_length=100)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.box


class RosePacking(models.Model):
	packing = models.CharField(max_length=100)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.packing


class RoseColour(models.Model):
	colour = models.CharField(max_length=50)
	status = models.BooleanField(default=False)

	def __str__(self):
		return str(self.colour)


class RoseAmount(models.Model):
	rose_amount = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(1000)])

	def __str__(self):
		return str(self.rose_amount)


class BucketsDetails(models.Model):
	order_id = models.IntegerField()
	colours = models.CharField(max_length=150, blank=True, null=False)
	rose_amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	packing = models.CharField(max_length=100, blank=True, null=True)
	rose_box = models.CharField(max_length=100, blank=True, null=True)
	price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	image = models.ImageField(upload_to='buckets/', null=True)


	def __str__(self):
		return f'id {self.id}'


class Order(models.Model):
	client_id = models.IntegerField(null=True, blank=True)
	number = models.IntegerField(null=True)
	total_price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	name_surname = models.CharField(max_length=50, default='', blank=True)
	address = models.CharField(max_length=50, default='', null=True, blank=True)
	phone = models.CharField(max_length=50, default='', null=True, blank=True)
	instagram = models.CharField(max_length=100, default='', null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	order_type = models.CharField(max_length=100, default='??????????????????')
	delivery_price = models.CharField(max_length=100, null=True, blank=True)
	given_date = models.DateTimeField(null=True)
	payment = models.CharField(max_length=100, null=True, blank=True, default='')
	order_status = models.CharField(max_length=100, default='?????????? ??????????????')
	from_where = models.CharField(max_length=100, blank=True, null=True, default='')
	anonymous = models.BooleanField(default=False)
	first_order = models.BooleanField(default=False)
	created_by = models.CharField(max_length=100, blank=True)
	description = models.CharField(max_length=300, default='')


	class Mera:
		ordering = ['-number']

	@staticmethod
	def get_orders_buckets(order_id):
		return BucketsDetails.objects.filter(order_id=order_id)

	def get_buckets_amount(self):
		buckets = BucketsDetails.objects.filter(order_id=self.id)
		return len(buckets)

	def __str__(self):
		return f'{self.number}'


class OrderStatus(models.Model):
	status = models.CharField(max_length=100)

	def __str__(self):
		return self.status


class OrderType(models.Model):
	type = models.CharField(max_length=100)

	def __str__(self):
		return self.type
