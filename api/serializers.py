from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Todo




class TodoSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Todo
        fields = ['url', 'id', 'author', 'state', 'name', 'description', 'created_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todo']