from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from eventmgr.mixins import ListViewLogin, CreateViewLogin, UpdateViewLogin, DeleteViewLogin
from .models import Contact
from .forms import ContactForm, ContactAddressFormSet, ContactPhoneFormSet, \
    ContactEmailFormSet


class ContactListView(ListViewLogin):
    model = Contact
    paginate_by = 25


class ContactCreateView(SuccessMessageMixin, CreateViewLogin):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')
    success_message = "Contact '%(name)s' created successfully."


class ContactUpdateView(SuccessMessageMixin, UpdateViewLogin):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')
    success_message = "Contact '%(name)s' updated successfully."


class ContactDeleteView(SuccessMessageMixin, DeleteViewLogin):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts')
    success_message = "Contact '%(name)s' deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class ContactAddressView(UpdateViewLogin):
    model = Contact
    form_class = ContactAddressFormSet
    success_url = reverse_lazy('contacts')

    def get_success_url(self):
        return self.success_url


class ContactPhoneView(UpdateViewLogin):
    model = Contact
    form_class = ContactPhoneFormSet
    success_url = reverse_lazy('contacts')

    def get_success_url(self):
        return self.success_url


class ContactEmailView(UpdateViewLogin):
    model = Contact
    form_class = ContactEmailFormSet
    success_url = reverse_lazy('contacts')

    def get_success_url(self):
        return self.success_url

