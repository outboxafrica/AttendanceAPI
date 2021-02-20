from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    "serializers registration requests and creates a new user"

    email = serializers.EmailField()
    username = serializers.CharField(trim_whitespace=True)
    password = serializers.CharField(
        max_length=16,
        write_only=True,
        required=True,
        error_messages={
            "required": "Password field is required",
            "blank": "Password field cannot be empty",
        }
    )

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)
