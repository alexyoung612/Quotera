from django.contrib import admin

from .models import Awning, AwningType, Quote, Customer, QuoteStatus

admin.site.register(Quote)
admin.site.register(QuoteStatus)
admin.site.register(Customer)
admin.site.register(Awning)
admin.site.register(AwningType)
