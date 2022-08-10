from django.urls import include, path
from seri import views
from rest_framework import routers

from seri.views import AlbumViewset, TrackViewset

router = routers.DefaultRouter()
router.register('album', viewset=AlbumViewset)
router.register('track', viewset=TrackViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('account/', views.AccountListCreateAPIView.as_view()),
    path('account/<str:account_name>/', views.AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-detail'),
    path('user/', views.TestUserListCreateAPIView.as_view()),
    path('user/<str:username>/', views.TestUserRetrieveUpdateDestroyAPIView.as_view(), name='testuser-detail'),
]
