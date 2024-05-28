from django.urls import path
from .views import SingUpView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

