# tutorial/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from snippets import views as sviews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include('class_based_api_views.urls')),
    path('snippets/', include('snippets.urls')),
    path('seri/', include('seri.urls')),
    path('login/', sviews.login),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', sviews.api_root),
]
