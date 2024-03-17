
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menus.urls')),
    path('inventory/', include('inventory.urls')),
    path('vendor/', include('vendor.urls')),
    path('customer/', include('customer.urls')),
    path('order/', include('order.urls')),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
