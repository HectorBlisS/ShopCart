from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^crear/$', views.CrearOrden.as_view(), name="crear"),
]
