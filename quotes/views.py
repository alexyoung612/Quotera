from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Quote

def index(request):
    latest_quote_list = Quote.objects.order_by('-date_created')[:5]
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'quotes/index.html', context)

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/detail.html', {'quote': quote})

def email_draft(request, quote_id):
    response = "You're looking at the email draft of quote %s."
    return HttpResponse(response % quote_id)
