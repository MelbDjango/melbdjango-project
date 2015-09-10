from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


""" derive generic views that have the login_required wrapper """


class ListViewLogin(LoginRequiredMixin, ListView):
    pass


class CreateViewLogin(LoginRequiredMixin, CreateView):
    pass


class UpdateViewLogin(LoginRequiredMixin, UpdateView):
    pass


class DeleteViewLogin(LoginRequiredMixin, DeleteView):
    pass

