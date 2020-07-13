from django.contrib import admin

from .models import Quote, Customer, QuoteStatus

admin.site.register(Quote)
admin.site.register(QuoteStatus)
admin.site.register(Customer)