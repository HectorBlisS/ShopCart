from django.conf.urls import url, include
from django.contrib import admin
from cart import urls as cartUrls
from shop import urls as shopUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(cartUrls, namespace="cart")),
    url(r'^', include(shopUrls, namespace="shop")),
]
