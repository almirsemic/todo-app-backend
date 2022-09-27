from api.models import Todo
from api.serializers import TodoSerializer, UserSerializer
from rest_framework import viewsets, permissions, renderers
from django.contrib.auth.models import User
from api.permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
   
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
