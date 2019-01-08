from django.urls import path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="chat/lobby.html"), name="index"),
]
