from django.contrib import admin
from django.urls import path, include
import scp_series.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(scp_series.urls)),
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
]
