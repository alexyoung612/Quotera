from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Quote

@login_required
def email_draft(request, quote_id):
    response = "You're looking at the email draft of quote %s."
    return HttpResponse(response % quote_id)

class QuoteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'quotes.add_quote'
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

class QuoteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'quotes.change_quote'
    permission_denied_message = 'You do not have permission to update quotes'
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

class QuoteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'quotes.view_quote'
    queryset = Quote.objects.order_by('-created_at')[:5]
