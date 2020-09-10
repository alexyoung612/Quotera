from django.contrib import admin

from .models import (
    Awning, AwningOperation, AwningType, AwningMotorType, AwningCordLength,
    AwningRemote, AwningCrankSize, AwningHoodCover, AwningValance, AwningMount,
    AwningBracketType, Quote, Customer, QuoteStatus
)

admin.site.register(Quote)
admin.site.register(QuoteStatus)
admin.site.register(Customer)
admin.site.register(Awning)
admin.site.register(AwningType)
admin.site.register(AwningOperation)
admin.site.register(AwningMotorType)
admin.site.register(AwningCordLength)
admin.site.register(AwningRemote)
admin.site.register(AwningCrankSize)
admin.site.register(AwningHoodCover)
admin.site.register(AwningValance)
admin.site.register(AwningMount)
admin.site.register(AwningBracketType)
