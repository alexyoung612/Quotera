import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit, Row
from crispy_forms.bootstrap import PrependedText
from django import forms
from django.forms.models import inlineformset_factory

from .custom_layout_object import Formset
from .models import Awning, Customer, Screen, Quote


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'address', 'city', 'phone', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_hidden_fields = True
        self.helper.layout = Layout(
            Div(
                Row(
                    Field('name', wrapper_class='col-md'),
                    Field('address', wrapper_class='col-md'),
                    Field('city', wrapper_class='col-md'),
                    Field('phone', wrapper_class='col-md'),
                    Field('email', wrapper_class='col-md'),
                    # Field('DELETE', wrapper_class='col-md-2'),
                ),
                css_class='formset_row-{}'.format(formtag_prefix)
            )
        )

CustomerFormSet = inlineformset_factory(
    Quote, Customer, form=CustomerForm,
    fields=['name', 'address', 'city', 'phone', 'email'], extra=1, min_num=1,
    max_num=1, can_delete=False
)

class AwningForm(forms.ModelForm):

    class Meta:
        model = Awning
        fields = ('awning_type', 'quote',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_hidden_fields = True
        self.helper.layout = Layout(
            Div(
                Row(
                    Field('awning_type', wrapper_class='col-md-9'),
                    Field('wrap_front_profile'),
                ),
                Row(
                    Field('width_inches', wrapper_class='col-md-3'),
                    Field('projection_inches', wrapper_class='col-md-3'),
                    Field('height_inches', wrapper_class='col-md-3'),
                    Field('frame_color', wrapper_class='col-md-3'),
                ),
                Row(
                    Field('operation', wrapper_class='col-md-2'),
                    Field('motor_type', wrapper_class='col-md-2'),
                    Field('cord_length', wrapper_class='col-md-2'),
                    Field('remote', wrapper_class='col-md-2'),
                    Field('wind_sensor', wrapper_class='col-md-2'),
                    Field('crank_size', wrapper_class='col-md-2'),
                ),
                Row(
                    Field('control_side', wrapper_class='col-md-2'),
                    Field('control_notes', wrapper_class='col-md-2'),
                    Field('hood_cover', wrapper_class='col-md-2'),
                    Field('fabric', wrapper_class='col-md-2'),
                    Field('valance', wrapper_class='col-md-2'),
                    Field('trim', wrapper_class='col-md-2'),
                ),
                Row(
                    Field('mount', wrapper_class='col-md-3'),
                    Field('mount_notes', wrapper_class='col-md-9'),
                ),
                Row(
                    Field('bracket_type', wrapper_class='col-md-4'),
                    Field('bracket_quantity', wrapper_class='col-md-4'),
                    Field('bracket_color', wrapper_class='col-md-4'),
                ),
                Row(
                    Field('placement_on_house', wrapper_class='col-md-2'),
                    Field('awning_notes', wrapper_class='col-md-10', rows='3'),
                ),
                Row(
                    PrependedText('awning_price_quote', '$', wrapper_class='col-md-3'),
                    PrependedText('motor_price_quote', '$', wrapper_class='col-md-3'),
                    PrependedText('bracket_price_quote', '$', wrapper_class='col-md-3'),
                    PrependedText('additional_costs_quote', '$', wrapper_class='col-md-3'),
                ),
                Field('DELETE'),
                css_class='formset_row-{} list-group-item rounded'.format(formtag_prefix)
            ),
        )

AwningFormSet = inlineformset_factory(
    Quote, Awning, form=AwningForm,
    fields=[
        'awning_type', 'wrap_front_profile', 'width_inches',
        'projection_inches', 'height_inches', 'frame_color', 'operation',
        'motor_type', 'cord_length', 'remote', 'wind_sensor', 'crank_size',
        'control_side', 'control_notes', 'hood_cover', 'fabric', 'valance',
        'trim', 'mount', 'mount_notes', 'bracket_type', 'bracket_quantity',
        'bracket_color', 'placement_on_house', 'awning_notes',
        'awning_price_quote', 'motor_price_quote', 'bracket_price_quote',
        'additional_costs_quote'
    ], extra=1, can_delete=True
)

class ScreenForm(forms.ModelForm):

    class Meta:
        model = Screen
        fields = ('fabric_color', 'quote',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.render_hidden_fields = True
        self.helper.layout = Layout(
            Row(
                Field('fabric_color'),
                Field('DELETE'),
                css_class='formset_row-{}'.format(formtag_prefix)
            )
        )

ScreenFormSet = inlineformset_factory(
    Quote, Screen, form=ScreenForm, fields=['fabric_color'], extra=1,
    can_delete=True
)

class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = (
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
                Fieldset(
                    'Customer Information',
                    Formset('customers')
                ),
                Fieldset(
                    'Awnings',
                    Formset('awnings'),
                    css_class='list-group'
                ),
                Fieldset(
                    'Screens',
                    Formset('screens')
                ),
                Field('estimated_install_time'),
                Field('install_difficulty'),
                Field('installers_required'),
                Field('equipment_required'),
                Field('status'),
                HTML('<br>'),
                ButtonHolder(
                    Submit('submit', 'save'),
                    # Possibly move this element outside of the form in the future?
                    HTML('<a href="{% url \'quotes:email_preview\' quote_id=quote.pk %}" class="btn btn-success float-right" role="button" aria-pressed="true">Preview Email</a>')
                ),
            )
        )
