from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction

from .models import Quote
from .forms import AwningFormSet, QuoteForm

@login_required
def email_draft(request, quote_id):
    response = "You're looking at the email draft of quote %s."
    return HttpResponse(response % quote_id)

class QuoteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    permission_required = 'quotes.add_quote'
    model = Quote
    form_class = QuoteForm

    def get_context_data(self, **kwargs):
        data = super(QuoteCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['awnings'] = AwningFormSet(self.request.POST)
        else:
            data['awnings'] = AwningFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        awnings = context['awnings']
        with transaction.atomic():
            form.instance.written_by = self.request.user
            self.object = form.save()
            if awnings.is_valid():
                awnings.instance = self.object
                awnings.save()
        return super(QuoteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('quotes:detail', args=[str(self.object.id)])

class QuoteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'quotes.change_quote'
    permission_denied_message = 'You do not have permission to update quotes'
    model = Quote
    form_class = QuoteForm

    def get_context_data(self, **kwargs):
        data = super(QuoteUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['awnings'] = AwningFormSet(self.request.POST, instance=self.object)
        else:
            data['awnings'] = AwningFormSet(instance=self.object)
        return data

    def get_object(self, queryset=None):
        quote_id = self.kwargs.get('quote_id')
        return get_object_or_404(Quote, pk=quote_id)

    def form_valid(self, form):
        context = self.get_context_data()
        awnings = context['awnings']
        with transaction.atomic():
            form.instance.written_by = self.request.user
            self.object = form.save()
            if awnings.is_valid():
                awnings.instance = self.object
                awnings.save()
        return super(QuoteUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('quotes:detail', args=[str(self.object.id)])

class QuoteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'quotes.view_quote'
    queryset = Quote.objects.order_by('-created_at')[:5]
