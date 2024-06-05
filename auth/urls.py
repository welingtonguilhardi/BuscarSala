# auth/auth/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),  # Inclua o aplicativo usuario
    path('',include('home.urls'))
]




