from django.urls import path

from chat.views import ChatRoomView, LobbyView


urlpatterns = [
    path('', LobbyView.as_view(), name="lobby"),
    path('<str:room_name>/', ChatRoomView.as_view(), name="chat_room"),
]
