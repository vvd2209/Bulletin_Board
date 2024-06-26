from django.urls import path
from rest_framework import routers

from ads.views import AdViewSet, AdListAPIView, AdCreateAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView, CommentViewSet

app_name = "ads"

router = routers.SimpleRouter()
router.register('ads', AdViewSet, basename="ads")
router.register('comments', CommentViewSet, basename="comments")

urlpatterns = [
    path('list/', AdListAPIView.as_view(), name='ad_list'),
    path('view/<int:pk>/', AdRetrieveAPIView.as_view(), name='ad_view'),
    path('create/', AdCreateAPIView.as_view(), name='ad_create'),
    path('update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
    path('delete/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_delete'),
] + router.urls
