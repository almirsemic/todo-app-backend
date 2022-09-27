from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'todo', views.TodoViewSet,basename="todo")
router.register(r'users', views.UserViewSet,basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
