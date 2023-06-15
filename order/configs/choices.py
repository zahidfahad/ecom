from django.db import models

class OrderStatus(models.TextChoices):
    NEW = 'new'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    PICKED_BY_DELIVERY_MAN = 'picked_by_delivery_man'
    DELIVERED = 'delivered'