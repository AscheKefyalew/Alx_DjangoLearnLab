from django.urls import path
from .views import UserRegisterView, UserLoginView, FollowViewSet

# Define the viewsets first
follow_viewset = FollowViewSet.as_view({
    'post': 'follow'
})

unfollow_viewset = FollowViewSet.as_view({
    'post': 'unfollow'
})

# Then use them in urlpatterns
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('follow/<int:pk>/', follow_viewset, name='follow_user'),
    path('unfollow/<int:pk>/', unfollow_viewset, name='unfollow_user'),
]
