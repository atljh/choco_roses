from django.db import models
from django.contrib.auth.models import User
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





class RoseColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class RoseAmount(models.Model):
    amount = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(1000)])

    def __str__(self):
        return str(self.amount)



class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    color = models.ForeignKey(RoseColor, on_delete=models.CASCADE, default=1)
    amount = models.ForeignKey(RoseAmount, on_delete=models.CASCADE, default=1)
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


class Order(models.Model):
    CHOICES = (
        ('PICKUP', 'PICKUP'),
        ('DELIVERY', 'DELIVERY')
    )
    STATUS = (
        ('In process', 'In process'),
        ('Packed', 'Packed'),
        ('Delivering', 'Delivering'),
        ('Done', 'Done')
    )
    # number = models.IntegerField(default=0)
    color = models.ForeignKey(RoseColor, on_delete=models.CASCADE, default=1, blank=True, related_name='color1')
    color2 = models.ForeignKey(RoseColor, null=True, on_delete=models.CASCADE, blank=True, related_name='color2')
    color3 = models.ForeignKey(RoseColor, null=True, on_delete=models.CASCADE, blank=True, related_name='color3')
    amount = models.ForeignKey(RoseAmount, on_delete=models.CASCADE, default=1)
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    name = models.CharField(max_length=50, default='', blank=True)
    surname = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100, choices=CHOICES, default='PICKUP')
    status = models.CharField(max_length=100, choices=STATUS, default='In process')
    # status = models.BooleanField(default=False)
    description = models.CharField(max_length=300, default='')

    def order_save(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    def __str__(self):
        return str(self.id)
