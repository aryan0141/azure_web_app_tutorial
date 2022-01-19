from django.urls import path
from .views import UserProfileAPIView, UserRegistrationAPIView, UserLogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('profile/', UserProfileAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationAPIView.as_view()),
    path('logout/', UserLogoutAPIView.as_view()),
]
