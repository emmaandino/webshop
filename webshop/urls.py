from django.contrib import admin
from django.urls import path, include
from entidad.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #para que cuando se entre a la pag normal nos dirija al index
    path("", index, name="index"),
    path('admin/', admin.site.urls),
    path('entidad/', include("entidad.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
