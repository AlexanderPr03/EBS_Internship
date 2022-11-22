from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = router.urls

from apps.users.views import RegisterUserView, MyObtainTokenPairView, UserListView

urlpatterns += [
    path('users/', UserListView.as_view(), name = 'user_list'),
    path('register/', RegisterUserView.as_view(), name='token_register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
