from django.contrib import admin
from django.urls import path, include
from api.views import ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
