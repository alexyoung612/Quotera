from django.http import HttpResponse
from django.shortcuts import render
from .models import Quote

def index(request):
    latest_quote_list = Quote.objects.order_by('-date_created')[:5]
    output = ', '.join([str(q.pk) for q in latest_quote_list])
    return HttpResponse(output)

def detail(request, quote_id):
    return HttpResponse("You're looking at quote %s." % quote_id)

def email_draft(request, quote_id):
    response = "You're looking at the email draft of quote %s."
    return HttpResponse(response % quote_id)
