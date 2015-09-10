from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


class RootRedirectView(RedirectView):
#   url = reverse_lazy('events')
    url = reverse_lazy('contacts')
    permanent = True

