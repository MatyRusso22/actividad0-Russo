from django.contrib import admin
from django.urls import include, path
from polls.views import IndexView  # Importa la vista IndexView de la aplicación de encuestas

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # Usa la vista IndexView para la ruta raíz
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
