from django.urls import path, include
from django.contrib import admin

from contacts.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/', include('contacts.urls')),
    path('v2/', include(router.urls))
]