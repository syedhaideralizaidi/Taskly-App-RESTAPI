from django.conf import settings
from django.contrib import admin
from django.urls import path , include , re_path

from users import router as users_api_router
from house import routers as house_api_router
from tasks import router as tasks_api_router

from django.conf.urls.static import static

auth_api_urls = [
    re_path(r'', include('drf_social_oauth2.urls')),
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))


api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls)),
    path(r'house/', include(house_api_router.router.urls)),
    path(r'tasks/', include(tasks_api_router.router.urls)),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)