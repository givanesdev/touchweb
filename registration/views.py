from django.shortcuts import render
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms import layout
from django.views.generic.edit import FormView
from django.http import JsonResponse
from .urls import app_name
import django.core.validators as vd
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from . import models

class RegistrationForm(forms.Form):
    dsp_full_name = forms.CharField(
        label="Name",
        required=True,
        max_length=100
    )
    dsp_tel_no = forms.CharField(
        label="Telephone",
        required=True,
        max_length=15
    )
    latitude = forms.FloatField(
        label="Latitude",
        required=True
    )
    longitude = forms.FloatField(
        label="Longitude",
        required=True
    )
    point_of_sale = forms.CharField(
        label="Point of Sale",
        required=True,
        max_length=100
    )
    address_of_sale = forms.CharField(
        label="Address of P.O.S",
        required=True,
        max_length=100
    )
    owner_full_name = forms.CharField(
        label = "Name",
        required=True,
        max_length=100
    )
    owner_tel_no = forms.CharField(
        label= "Telephone",
        required=True,
        max_length=100
    )
    owner_id_number = forms.CharField(
        label= "Identification number (ID)",
        required=True,
        max_length=8,
        min_length=7
    )
    business_no = forms.CharField(
        label= "Business number",
        required=True,
        max_length=100
    )
    kra_pin = forms.CharField(
        label= "KRA pin",
        required=True,
        max_length=100
    )
    sup_full_name = forms.CharField(
        label = "Name",
        required=True,
        max_length=100
    )
    sup_tel_no = forms.CharField(
        label= "Telephone",
        required=True,
        max_length=100
    )
    sup_id_number = forms.CharField(
        label= "Identification number (ID)",
        required=True,
        max_length=8,
        min_length=7
    )
    cashier_full_name = forms.CharField(
        label = "Name",
        required=True,
        max_length=100
    )
    cashier_tel_no = forms.CharField(
        label= "Telephone",
        required=True,
        max_length=100
    )
    cashier_id_number = forms.CharField(
        label= "Identification number (ID)",
        required=True,
        max_length=8,
        min_length=7
    )
    products = forms.ChoiceField(
        label="Select Product to market",
        choices=(("1", "Payment of bills"), ("2", "Mobile money"), ("3", "Airtime"), ("4", "Money transfer"), ("5", "Insurance"))
    )
    imei = forms.CharField(
        label = "IMEI",
        required=True
    )
    serial = forms.CharField(
        label = "Serial no",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "registrationForm"
        self.helper.add_input(layout.Submit('submit', 'Submit'))
        self.fields.get("latitude").widget.attrs['readonly'] = True
        self.fields.get("longitude").widget.attrs['readonly'] = True
        self.helper.layout = layout.Layout(
            layout.Row(
                layout.Column(
                    layout.Fieldset(
                        "Client details",
                        "owner_full_name",
                        "owner_tel_no",
                        "owner_id_number",
                        "kra_pin",
                        "imei",
                        "serial"
                    ),
                    layout.Fieldset(
                        "Cashier details",
                        "cashier_full_name",
                        "cashier_tel_no",
                        "cashier_id_number"
                    ), css_class="form-group col-lg-4"  
                ),
                layout.Column(
                    layout.Fieldset(
                        "Business information",
                        "point_of_sale",
                        "address_of_sale",
                        "business_no",
                        "products",
                        layout.Row(
                            "latitude",
                            "longitude"
                        )
                    ),css_class="form-group col-lg-4"
                ),
                layout.Column(
                    layout.Fieldset(
                        "Supervisor details",
                        "sup_full_name",
                        "sup_tel_no",
                        "sup_id_number"
                    ),
                    layout.Fieldset(
                    "Salesperson details",
                    "dsp_full_name",
                    "dsp_tel_no"
                    ), css_class="form-group col-lg-4"
                ),
            ),
        )


DEFAULT_FORM = {
    "dsp_full_name" : "Jeremy Awendo",
    "dsp_tel_no": "0798510126",
    "location": "Kiambu",
    "point_of_sale": "Muran'ga",
    "address_of_sale": "23017 Thika",
    "owner_full_name": "James Auoko",
    "owner_tel_no": "0754235214",
    "owner_id_number": "24589635",
    "business_no": "JFk54455L",
    "kra_pin": "A0134554633",
    "sup_full_name": "Chris Wanyoike",
    "sup_tel_no": "0741214579",
    "sup_id_number": "1965441",
    "cashier_full_name": "Jennifer Mutembei",
    "cashier_tel_no": "0775984258",
    "cashier_id_number": "31256897",
    "products": "2",
}


class IndexPage(LoginRequiredMixin, FormView):
    form_class = RegistrationForm
    template_name = "registration/index.html"
    login_url = "/backoffice/login"

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(initial=DEFAULT_FORM)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        dsp_full_name  = form.cleaned_data.get("dsp_full_name")
        dsp_tel_no  = form.cleaned_data.get("dsp_tel_no")
        latitude  = form.cleaned_data.get("latitude")
        longitude  = form.cleaned_data.get("longitude")
        point_of_sale  = form.cleaned_data.get("point_of_sale")
        address_of_sale  = form.cleaned_data.get("address_of_sale")
        owner_full_name  = form.cleaned_data.get("owner_full_name")
        owner_tel_no  = form.cleaned_data.get("owner_tel_no")
        owner_id_number  = form.cleaned_data.get("owner_id_number")
        business_no  = form.cleaned_data.get("business_no")
        kra_pin  = form.cleaned_data.get("kra_pin")
        sup_full_name  = form.cleaned_data.get("sup_full_name")
        sup_tel_no  = form.cleaned_data.get("sup_tel_no")
        sup_id_number  = form.cleaned_data.get("sup_id_number")
        cashier_full_name  = form.cleaned_data.get("cashier_full_name")
        cashier_tel_no  = form.cleaned_data.get("cashier_tel_no")
        cashier_id_number  = form.cleaned_data.get("cashier_id_number")
        products  = form.cleaned_data.get("products")
        imei  = form.cleaned_data.get("imei")
        serial  = form.cleaned_data.get("serial")
        obj = models.Registration(
            dsp_full_name=dsp_full_name,
            dsp_tel_no=dsp_tel_no,
            latitude=latitude,
            longitude=longitude,
            point_of_sale=point_of_sale,
            address_of_sale=address_of_sale,
            owner_full_name=owner_full_name,
            owner_tel_no=owner_tel_no,
            owner_id_number=owner_id_number,
            business_no=business_no,
            kra_pin=kra_pin,
            sup_full_name=sup_full_name,
            sup_tel_no=sup_tel_no,
            sup_id_number=sup_id_number,
            cashier_full_name=cashier_full_name,
            cashier_tel_no=cashier_tel_no,
            cashier_id_number=cashier_id_number,
            products=products,
            imei=imei,
            serial=serial
            )
        obj.save()
        return render(self.request, "registration/success.html")

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})