from django.urls import path, include
# from .views import UserList
# from .views import UserDetails
# from .views import GroupList
from .views import UsersAPIView, UserRegistrationAPIView, UserLogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/profile/', UsersAPIView.as_view()),
    # path('users/<pk>/', UserDetails.as_view()),
    # path('groups/', GroupList.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', UserRegistrationAPIView.as_view()),
    path('users/logout/', UserLogoutAPIView.as_view()),
]
