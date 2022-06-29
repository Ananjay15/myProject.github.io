from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('',include('authentication.urls')),
    path('',include('accounts.urls')),
    path('',include('composeEmail.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('djga/', include('google_analytics.urls')),
    path('admin_tools/', include('admin_tools.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
