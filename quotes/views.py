from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse

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

class QuoteCreateView(CreateView):
    model = Quote
    fields = (
        'customers',
        'estimated_install_time',
        'install_difficulty',
        'installers_required',
        'equipment_required',
        'status',
    )

    def form_valid(self, form):
        form.instance.written_by = self.request.user
        return super(QuoteCreateView, self).form_valid(form)

    def get_success_url(self):
            return reverse('quotes:detail', args=[str(self.object.id)])

class QuoteUpdateView(UpdateView):
    model = Quote
    fields = (
        'customers',
        'estimated_install_time',
        'install_difficulty',
        'installers_required',
        'equipment_required',
        'status',
    )

    def get_object(self):
        quote_id = self.kwargs.get('quote_id')
        return get_object_or_404(Quote, pk=quote_id)

    def form_valid(self, form):
        return super(QuoteUpdateView, self).form_valid(form)

    def get_success_url(self):
            return reverse('quotes:detail', args=[str(self.object.id)])
