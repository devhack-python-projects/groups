from rest_framework import serializers

from . import models

class User(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'name'
        )


class Group(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = (
            'id',
            'name',
            #'author',
            'description',
            #'members',
        )


class Publication(serializers.ModelSerializer):

    class Meta:
        model = models.Publication
        fields = (
            'text',
            'group'
        )

class Comment(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = (
            'text',
            'publication'
        )
