from eventmgr.mixins import ListViewLogin
from .models import Event


class EventListView(ListViewLogin):
    model = Event
    template_name = 'events.html'
