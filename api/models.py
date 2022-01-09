from django.db import models
import uuid

# Models needed:
# products, order_items, orders


class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(decimal_places=2, max_digits=6)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return f"{self.name}"


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True, editable=False)
	status = models.CharField(max_length=10, default='NEW')  # NEW / PAID

	class Meta:
		ordering = ('status',)

	def __str__(self):
		return f"{self.id} - {self.status}"


class OrderItem(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, db_index=True, editable=False)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField()
	# Replacement product needs just the ID field from the Product model
	replacement_product = models.ForeignKey(
		Product, related_name="replacement_product", null=True, default=None, on_delete=models.SET_NULL
	)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return f"{self.id}"
