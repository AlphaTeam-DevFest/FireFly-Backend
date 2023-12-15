# yourprojectname/urls.py
from django.contrib import admin
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from core.views import LoginView, LogoutView, RegisterView, UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peaceApp.urls')),
]

router = DefaultRouter()
router.register(r'users', UserViewSet)

# JWT Token urls
urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Djoser urls
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view()),
    path('reset_password', auth_views.PasswordResetView.as_view(), name = "reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset/<uibd64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete")
]


# User urls
urlpatterns += router.urls
