from django.urls import path, include
import django.contrib.auth.urls
from . import views

app_name = 'accounts'

urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
        path('register/', views.CustomUserRegistration.as_view(), name='register'),
        path('redirect/', views.account_redirect, name='account-redirect'),
        path('update_profile/<int:pk>', views.CustomUserUpdateView.as_view(), 
                name='profile-update'),
        path('profile-redirect/', views.profile_update_redirect, 
                name='profile-update-redirect'),
        path('settings', views.UserSettingsView.as_view(), name='user-settings')
]
