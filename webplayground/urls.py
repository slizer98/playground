
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messeger.urls import messeger_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('profiles/', include(profiles_patterns)),
    path('messenger/', include(messeger_patterns)),
    path('admin/', admin.site.urls),
    # auths paths
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)