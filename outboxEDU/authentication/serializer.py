import re

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

    def validate_email(self, email):
        """
        Validates the email 
        """

        # filter object to find if email exists
        email_exist = User.objects.filter(email=email)
        if email_exist.exists():
            raise serializers.ValidationError('The email already exists')
        return email

    def validate_username(self, username):
        """
        Validates the username 
        """

        # filter object to find if username exists
        username_exists = User.objects.filter(username=username)
        if username_exists.exists():
            raise serializers.ValidationError('The username already exists')
        if not username:
            raise serializers.ValidationError('Username should be provided')
        if len(username) <= 4:
            raise serializers.ValidationError(
                "username should be longer than 4 characters")
        if re.search(r'[\s]', username):
            raise serializers.ValidationError(
                "username should not contain spaces")
        if not re.search(r'[a-zA-Z]', username):
            raise serializers.ValidationError(
                "username should contain characters")
        return username

    def validate_password(self, password):
        """
        Validates the password 
        """
        if len(password) < 8:
            raise serializers.ValidationError(
                "password cannot be less than 8 characters")
        if re.search(r'[\s]', password):
            raise serializers.ValidationError(
                "Password should not contain spaces")
        return password

    class Meta:
        model = User
        # fields that could be used in request or response

        fields = ["email", "username", "password"]

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)
