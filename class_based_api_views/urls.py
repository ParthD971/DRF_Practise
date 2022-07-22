from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from class_based_api_views import views


urlpatterns = [
    path('transformers/', views.TransformerList.as_view()),
    path('transformers/<int:pk>/', views.TransformerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
