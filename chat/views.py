from django.utils.safestring import mark_safe
from django.views.generic.base import TemplateView


class LobbyView(TemplateView):
    template_name = 'chat/lobby.html'


class ChatRoomView(TemplateView):
    template_name = 'chat/room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_name_json'] = mark_safe(kwargs.get('room_name'))
        return context
