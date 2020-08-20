from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class QuoteStatus(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Quote - Statuses'

    def __str__(self):
        return self.name

class Quote(models.Model):
    estimated_install_time = models.CharField(max_length=100)
    install_difficulty = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    installers_required = models.PositiveIntegerField()
    equipment_required = models.CharField(max_length=200)
    written_by = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(QuoteStatus, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    quote = models.ForeignKey(Quote, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AwningType(models.Model):
    name = models.CharField(max_length=40, unique=True)
    can_wrap_front_profile = models.BooleanField(default=False)
    can_set_height = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AwningOperation(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningMotorType(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningCordLength(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningRemote(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningCrankSize(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningHoodCover(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningValance(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningMount(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class AwningBracketType(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Awning(models.Model):

    class AwningControlSide(models.IntegerChoices):
        LEFT = 0, _('Left')
        RIGHT = 1, _('Right')

        __empty__ = _('(Unknown)')

    class PlacementOnHouse(models.IntegerChoices):
        FRONT = 0, _('Front')
        BACK = 1, _('Back')
        RIGHT_SIDE = 2, _('Right Side')
        LEFT_SIDE = 3, _('Left Side')

        __empty__ = _('(Unknown)')

    quote = models.ForeignKey(Quote, on_delete=models.PROTECT)
    awning_type = models.ForeignKey(AwningType, on_delete=models.PROTECT)
    wrap_front_profile = models.BooleanField(default=False)
    width_inches = models.DecimalField(
        default=0, decimal_places=2, max_digits=5, validators=[MinValueValidator(0)]
    )
    projection_inches = models.DecimalField(
        default=0, decimal_places=2, max_digits=5, validators=[MinValueValidator(0)]
    )
    height_inches = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=5,
        validators=[MinValueValidator(0)]
    )
    frame_color = models.CharField(max_length=30, default='white')
    operation = models.ForeignKey(AwningOperation, null=True, on_delete=models.PROTECT)
    motor_type = models.ForeignKey(
        AwningMotorType, null=True, blank=True, on_delete=models.PROTECT
    )
    cord_length = models.ForeignKey(
        AwningCordLength, null=True, blank=True, on_delete=models.PROTECT
    )
    remote = models.ForeignKey(
        AwningRemote, null=True, blank=True, on_delete=models.PROTECT
    )
    wind_sensor = models.BooleanField(default=False)
    crank_size = models.ForeignKey(
        AwningCrankSize, null=True, blank=True, on_delete=models.PROTECT
    )
    control_side = models.IntegerField(choices=AwningControlSide.choices)
    control_notes = models.CharField(max_length=255, blank=True)
    hood_cover = models.ForeignKey(
        AwningHoodCover, null=True, on_delete=models.PROTECT
    )
    fabric = models.CharField(max_length=30, blank=True)
    valance = models.ForeignKey(
        AwningValance, null=True, on_delete=models.PROTECT
    )
    trim = models.CharField(max_length=30, blank=True)
    mount = models.ForeignKey(AwningMount, null=True, on_delete=models.PROTECT)
    mount_notes = models.CharField(max_length=255, blank=True)
    bracket_type = models.ForeignKey(
        AwningBracketType, null=True, blank=True, on_delete=models.PROTECT
    )
    bracket_quantity = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    bracket_color = models.CharField(blank=True, max_length=30)
    placement_on_house = models.IntegerField(choices=PlacementOnHouse.choices)
    awning_notes = models.TextField(blank=True)
    awning_price_quote = models.DecimalField(
        default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(0)]
    )
    motor_price_quote = models.DecimalField(
        default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(0)]
    )
    bracket_price_quote = models.DecimalField(
        default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(0)]
    )
    additional_costs_quote = models.DecimalField(
        default=0, decimal_places=2, max_digits=8, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.awning_type.name} \
            {self.width_inches}x{self.projection_inches}x{self.height_inches}"

class Screen(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.PROTECT)
    fabric_color = models.CharField(max_length=20)
