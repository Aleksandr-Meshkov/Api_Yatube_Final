from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_api_v1 = routers.DefaultRouter()
router_api_v1.register('posts', PostViewSet, basename='posts')
router_api_v1.register('follow', FollowViewSet, basename='follow')
router_api_v1.register('groups', GroupViewSet, basename='groups')
router_api_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
