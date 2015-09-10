from django.forms import models, inlineformset_factory
from .models import Contact, Address, Email, PhoneNumber


class BootstrapForm(models.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        This is an ugly hack, but it works;
        way better than adding widgets for every field!
        """
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class ContactForm(BootstrapForm):

    class Meta:
        model = Contact
        fields = ['title', 'name', 'nick', 'company']
        labels = {
            'nick': 'Nickname',
            'company': 'Company?'
        }
        help_texts = {
            'name': 'Contact\'s full name',
            'nick': 'Contact\'s nickname, or leave blank',
            'company': 'Check this if this contact is a company, not a person'
        }


class AddressForm(BootstrapForm):

    class Meta:
        model = Address
        fields = ['type', 'address_1', 'address_2', 'locality', 'title']
        labels = {
            'type': 'Address Type',
            'title': 'Address Label',
        }
        help_texts = {
            'type': 'Select an appropriate address type',
            'address_1': 'Enter first address line (required)',
            'address_2': 'Enter second address line (optional)',
            'locality': 'Select the address locality',
            'title': 'Enter an optional name for this address or leave blank',
        }


ContactAddressFormSet = inlineformset_factory(Contact, Address, form=AddressForm)


class EmailForm(BootstrapForm):

    class Meta:
        model = Email
        fields = ['type', 'address']
        labels = {
            'type': 'Email Type',
            'address': 'Email Address'
        }
        help_texts = {
            'type': 'Select a type that describes the email address',
            'address': 'Contact\'s email address in username@domain format'
        }


ContactEmailFormSet = inlineformset_factory(Contact, Email, form=EmailForm)


class PhoneForm(BootstrapForm):

    class Meta:
        model = PhoneNumber
        fields = ['type', 'number']
        labels = {
            'type': 'Phone Type',
            'number': 'Phone Number'
        }
        help_texts = {
            'type': 'Select an appropriate phone number type',
            'number': 'Enter the phone number (localised or with +country prefix)',
        }


ContactPhoneFormSet = inlineformset_factory(Contact, PhoneNumber, form=PhoneForm)
