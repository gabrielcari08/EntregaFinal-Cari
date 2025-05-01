from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView, ProfileView, EditProfileView, WelcomeView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(next_page='welcome'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
]
