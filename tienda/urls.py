from django.contrib import admin
from django.urls import path, include
from usuarios import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', user_views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/registro.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('productos/', include('productos.urls', namespace='productos')),
    path('carrito/', include('carrito.urls', namespace='carrito')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
