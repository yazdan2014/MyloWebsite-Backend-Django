from rest_framework import serializers


class CommandsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    aliases = serializers.CharField(max_length=255)
    field = serializers.CharField(max_length=255)


class ArticlesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.JSONField()
    tags = serializers.CharField(max_length=100)
    date = serializers.DateField()
