
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productsapp.urls')),
    path('account/login/',obtain_auth_token) #authentication
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
