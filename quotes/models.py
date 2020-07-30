from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class QuoteStatus(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Quote - Statuses'

    def __str__(self):
        return self.name

class Quote(models.Model):
    estimated_install_time = models.CharField(max_length=100)
    install_difficulty = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    installers_required = models.IntegerField()
    equipment_required = models.CharField(max_length=200)
    written_by = models.ForeignKey(User, on_delete=models.PROTECT)
    customers = models.ManyToManyField(Customer)
    status = models.ForeignKey(QuoteStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AwningType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Awning(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.PROTECT)
    awning_type = models.ForeignKey(AwningType, on_delete=models.PROTECT)

    def __str__(self):
        return self.awning_type.name
