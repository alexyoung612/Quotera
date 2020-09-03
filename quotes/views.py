from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction

from .models import Quote
from .forms import AwningFormSet, CustomerFormSet, ScreenFormSet, QuoteForm

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
            data['customers'] = CustomerFormSet(self.request.POST)
            data['awnings'] = AwningFormSet(self.request.POST)
            data['screens'] = ScreenFormSet(self.request.POST)
        else:
            data['customers'] = CustomerFormSet()
            data['awnings'] = AwningFormSet()
            data['screens'] = ScreenFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        customers = context['customers']
        awnings = context['awnings']
        screens = context['screens']

        with transaction.atomic():
            form.instance.written_by = self.request.user
            self.object = form.save()
            if awnings.is_valid() and screens.is_valid() and customers.is_valid():
                customers.instance = self.object
                customers.save()
                awnings.instance = self.object
                awnings.save()
                screens.instance = self.object
                screens.save()

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
            data['customers'] = CustomerFormSet(self.request.POST, instance=self.object)
            data['awnings'] = AwningFormSet(self.request.POST, instance=self.object)
            data['screens'] = ScreenFormSet(self.request.POST, instance=self.object)
        else:
            data['customers'] = CustomerFormSet(instance=self.object)
            data['awnings'] = AwningFormSet(instance=self.object)
            data['screens'] = ScreenFormSet(instance=self.object)
        return data

    def get_object(self, queryset=None):
        quote_id = self.kwargs.get('quote_id')
        return get_object_or_404(Quote, pk=quote_id)

    def form_valid(self, form):
        context = self.get_context_data()
        customers = context['customers']
        awnings = context['awnings']
        screens = context['screens']
        with transaction.atomic():
            form.instance.written_by = self.request.user
            self.object = form.save()
            if (
                awnings.is_valid() and screens.is_valid() and
                customers.is_valid()
            ):
                customers.instance = self.object
                customers.save()
                awnings.instance = self.object
                awnings.save()
                screens.instance = self.object
                screens.save()
        return super(QuoteUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('quotes:detail', args=[str(self.object.id)])

class QuoteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'quotes.view_quote'
    paginate_by = 10

    def get_queryset(self):

        # If user has permission to view all quotes, show all quotes from every user.
        # Otherwise, only show the most recent 10 created by the user.
        if self.request.user.has_perm('quotes.view_all_quotes'):
            return Quote.objects.order_by('-created_at')
        else:
            return Quote.objects.filter(written_by=self.request.user).order_by('-created_at')[:10]
