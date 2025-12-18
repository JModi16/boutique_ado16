from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country', 'county',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Force concrete choices to avoid BlankChoiceIterator __len__ issues
        self.fields['country'].choices = list(self.fields['country'].choices)
        if hasattr(self.fields['country'].widget, 'choices'):
            self.fields['country'].widget.choices = list(self.fields['country'].widget.choices)

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                placeholder = f"{placeholders[field]} *" if self.fields[field].required else placeholders[field]
                self.fields[field].widget.attrs.update({
                    'placeholder': placeholder,
                    'class': 'stripe-style-input'
                })
            else:
                self.fields[field].widget.attrs['class'] = 'custom-select d-block w-100'
            self.fields[field].label = False