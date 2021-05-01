from django.contrib import admin
from django.urls import path, include
import scp_series.urls
import accounts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(scp_series.urls)),
    path('account/', include(accounts.urls)),
]
