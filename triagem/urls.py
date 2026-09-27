from django.urls import path
from . import views

app_name = "triagem"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("questionario/", views.questionario, name="questionario"),
    path("resultado/", views.resultado, name="resultado"),
]
