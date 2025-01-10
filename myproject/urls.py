from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('index.urls')),  # Including URLs from the 'index' app
    path('base/', include('base.urls')),  # Including URLs from the 'base' app
    path('app1/', include('app1.urls')),  # Including URLs from the 'app1' app
    path('staff/', include('staff.urls')),  # Including URLs from the 'staff' app
]

# Add static and media URL patterns
# During development, Django will serve static and media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
