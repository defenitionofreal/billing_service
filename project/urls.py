from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from apps.base.api.token_view import MyObtainTokenPairView  # custom token info

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.base.urls', namespace='base')),
    path('api/v1/', include('apps.billing.urls', namespace='billing')),
    path('api/v1/token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
