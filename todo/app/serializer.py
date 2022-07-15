from rest_framework import serializers
from .models import Todo
from rest_framework.authtoken.models import Token


import logging

logger = logging.getLogger(__name__)


class Todoserializer(serializers.ModelSerializer):
    create_at = serializers.ReadOnlyField()
    #is_done = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields=["id","todo_title","todo_description","create_at","is_done","favourite"]

class todo_is_done_serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields=["id"]
        read_only_fields = ["user","todo_title","todo_description","create_at","is_done"]

class Todo_fav_serializer(serializers.ModelSerializer):
    # create_at = serializers.ReadOnlyField()
    # is_done = serializers.ReadOnlyField()
    # todo_description = serializers.ReadOnlyField()
    # todo_title = serializers.ReadOnlyField()
    # user = serializers.ReadOnlyField()
    class Meta:
        model = Todo
        fields=["id"]
       #read_only_fields = ["user","favourite","todo_title","todo_description","create_at","is_done"]



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    #token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = Token.objects.get_or_create(user=obj)[0]
        logger.error(token.key)
        return token.key


# class Todo_fav_Serializer(serializers.ModelSerializer):
#     