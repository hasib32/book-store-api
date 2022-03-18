from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        auth_user = self.context['request'].user
        return instance._meta.model.objects.update(auth_user, instance, **validated_data)