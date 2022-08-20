from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Client(models.Model):
	name = models.CharField(max_length=240)
	phone = models.CharField(max_length=14, null=True)
	instagram = models.CharField(max_length=50, null=True)
	address = models.CharField(max_length=300, null=True)
	email = models.EmailField(max_length=240, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('crm:detail-client', kwargs={'pk': self.pk})


class RoseColour(models.Model):
	colour = models.CharField(max_length=50)

	def __str__(self):
		return self.colour


class RoseAmount(models.Model):
	rose_amount = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(1000)])

	def __str__(self):
		return str(self.rose_amount)


class Product(models.Model):
	name = models.CharField(max_length=60)
	price = models.IntegerField(default=0)
	color = models.ForeignKey(RoseColour, on_delete=models.CASCADE, default=1)
	rose_amount = models.ForeignKey(RoseAmount, on_delete=models.CASCADE, default=1)
	description = models.CharField(
		max_length=250, default='', blank=True, null=True)
	image = models.ImageField(upload_to='products/')
	date_created = models.DateTimeField(auto_now_add=True)

	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in=ids)

	@staticmethod
	def get_all_products():
		return Product.objects.all()

	def __str__(self):
		return self.name


class RoseBoxes(models.Model):
	rose_box = models.CharField(max_length=100)

	def __str__(self):
		return self.rose_box


class RosePacking(models.Model):
	rose_packing = models.CharField(max_length=100)

	def __str__(self):
		return self.rose_packing


class BucketsDetails(models.Model):
	order_id = models.IntegerField()
	colours = models.CharField(max_length=150, blank=True, null=False)
	rose_amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	packing = models.CharField(max_length=100, blank=True, null=True)
	rose_box = models.CharField(max_length=100, blank=True, null=True)
	price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])

	def __str__(self):
		return f'id {self.id}'


class Order(models.Model):
	CHOICES = (
		('Самовывоз', 'Самовывоз'),
		('Доставка', 'Доставка')
	)
	STATUS = (
		('В процессе', 'В процессе'),
		('Упакован', 'Упакован'),
		('В пути', 'В пути'),
		('Доставлен', 'Доставлен'),
		('Отдан', 'Отдан')
	)

	number = models.IntegerField(null=True)
	total_price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
	name_surname = models.CharField(max_length=50, default='', blank=True)
	address = models.CharField(max_length=50, default='', null=True, blank=True)
	phone = models.CharField(max_length=50, default='', null=True, blank=True)
	instagram = models.CharField(max_length=100, default='', null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	order_type = models.CharField(max_length=100, choices=CHOICES, default='Самовывоз')
	delivery_data = models.CharField(max_length=100, null=True, blank=True)
	pickup_data = models.CharField(max_length=100, null=True, blank=True)
	payment = models.CharField(max_length=100, null=True, blank=True)
	order_status = models.CharField(max_length=100, default='В процессе`')
	from_where = models.CharField(max_length=100, blank=True, null=True)
	anonymous = models.BooleanField(default=False)
	first_order = models.BooleanField(default=False)
	created_by = models.CharField(max_length=100, blank=True)
	description = models.CharField(max_length=300, default='')

	def order_save(self):
		self.save()

	@staticmethod
	def get_orders_buckets(order_id):
		return BucketsDetails.objects.filter(order_id=order_id)

	def get_buckets_amount(self):
		buckets = BucketsDetails.objects.filter(order_id=self.id)
		return len(buckets)

	def __str__(self):
		return f'id {self.id}'
