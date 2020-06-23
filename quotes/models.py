from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Quote(models.Model):

    class QuoteStatus(models.TextChoices):
        AWAITING_EMAIL = 'EU', _('Awaiting Email')
        EMAIL_SENT = 'ES', _('Email Sent')
        PROJECT_COMPLETED = 'PC', _('Project Completed')
        INACTIVE = 'IN', _('Inactive')
        ARCHIVED = 'AR', _('Archived')

    estimated_install_time = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
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
    status = models.CharField(
        max_length = 2,
        choices=QuoteStatus.choices,
        default=QuoteStatus.AWAITING_EMAIL,
    )
