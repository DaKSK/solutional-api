from django.db import models

# Models needed:
# products, order_items, orders


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2, max_digits=6)


class Order(models.Model):
	id = models.UUIDField()
	status = models.CharField(max_length=10)  # NEW / PAID


class OrderItem(models.Model):
	id = models.UUIDField()
	order = models.ForeignKey(Order, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL)
	quantity = models.IntegerField()
	replaced_with = models.ForeignKey(Product, null=True, default=None, on_delete=models.DO_NOTHING, from_fields='id')


