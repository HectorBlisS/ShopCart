from __future__ import unicode_literals
from django.db import models
from shop.models import Product

class Order(models.Model):
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length=140)
	email = models.EmailField()
	fecha = models.DateTimeField(auto_now_add=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-fecha',)

	def __str__(self):
		return 'Orden {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(Product, related_name='order_items')
	price = models.DecimalField(max_digits=2, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity




