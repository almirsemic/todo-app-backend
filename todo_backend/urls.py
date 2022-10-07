from django.contrib import admin
from django.urls import path, include
from api.views import ChangePasswordView, UpdateProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),

]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
