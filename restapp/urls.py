from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('article/<int:pk>/', article_detail),
    path('article/<int:id>/', ArticleDetails.as_view()),
    path('generic/<int:id>/', GenericAPIView.as_view()),
]
