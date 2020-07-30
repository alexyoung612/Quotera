from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django import forms
from django.forms.models import inlineformset_factory

from .custom_layout_object import Formset
from .models import Awning, Quote

class AwningForm(forms.ModelForm):

    class Meta:
        model = Awning
        fields = ('awning_type', 'quote',)

AwningFormSet = inlineformset_factory(
    Quote, Awning, form=AwningForm, fields=['awning_type'], extra=1,
    can_delete=True
)

class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = (
            'customers',
            'estimated_install_time',
            'install_difficulty',
            'installers_required',
            'equipment_required',
            'status',
        )

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('customers'),
                Fieldset(
                    'Add awnings',
                    Formset('awnings')
                ),
                Field('estimated_install_time'),
                Field('install_difficulty'),
                Field('installers_required'),
                Field('equipment_required'),
                Field('status'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )