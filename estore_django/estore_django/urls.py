from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "eStore Admin"
admin.site.site_title = "eStore Admin Portal"
admin.site.index_title = "Welcome to eStore Adminstration Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
