from django.urls import include, path

urlpatterns = [
    path("", include("triagem.urls")),
]
