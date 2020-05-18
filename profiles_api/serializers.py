from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    "Serializer for post"
    name=serializers.CharField(max_length=10)
