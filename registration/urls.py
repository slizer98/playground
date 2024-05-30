from django.urls import path
from .views import SingUpView, ProfileUPdate, EmailUPdate
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('profile/', ProfileUPdate.as_view(), name="profile"),
    path('profile/email/', EmailUPdate.as_view(), name="profile_email"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

