# tutorial/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('class_based_api_views.urls')),
    path('', include('snippets.urls')),
]
