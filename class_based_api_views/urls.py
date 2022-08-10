from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from class_based_api_views import views
from rest_framework import routers


class CustomRootRouter(routers.DefaultRouter):
    root_view_name = 'api-root'


router = CustomRootRouter()
router.register(r'book-viewset', viewset=views.BookViewSet)
router.register(r'transformer-viewset', viewset=views.TransformerViewSet)


urlpatterns = [
    path('transformers/', views.TransformerList.as_view(), name='transformer-list'),
    path('transformers/<int:pk>/', views.TransformerDetail.as_view(), name='transformer-detail'),
    path('book/bulk/', views.BookBulkCreateUpdate.as_view(), name='book-bulk'),
    # path('book/bulk/', views.FooView.as_view(), name='book-bulk'),
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
