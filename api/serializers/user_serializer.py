from api.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            'id',
            'created_by',
            'email',
            'name',
            'password',
            'mobile_number',
            'is_active',
            'is_admin',
            'created_at',
            'last_login',
            'updated_at']

        extra_kwargs = {
            'is_active': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'is_admin': {'read_only': True},
            'created_by': {'read_only': True},
            'last_login': {'read_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
