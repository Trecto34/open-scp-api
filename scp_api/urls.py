from django.contrib import admin
from django.urls import path, include
from scp_series import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]
