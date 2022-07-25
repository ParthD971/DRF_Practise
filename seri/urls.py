from django.urls import include, path
from seri import views

urlpatterns = [
    path('account/', views.AccountListCreateAPIView.as_view()),
    path('account/<str:account_name>/', views.AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-detail'),
    path('user/', views.TestUserListCreateAPIView.as_view()),
    path('user/<str:username>/', views.TestUserRetrieveUpdateDestroyAPIView.as_view(), name='testuser-detail'),
]
