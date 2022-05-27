from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administrar/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('payments/', include('apps.pago.urls')),
]
