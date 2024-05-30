from django.urls import path
from .views import ProfileListView,ProfileDetail

profiles_patterns = ([
  path('', ProfileListView.as_view(), name="list"),
  path('<username>', ProfileDetail.as_view(), name="detail")
], 'profiles')