from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

USER = get_user_model()

class UserRegistrationSerializer(serializers.Serializer):

    """
    sign in serializer use to create new user 
    """

    email = serializers.EmailField()
    password = serializers.CharField()
    confirmPassword = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    
    def validate_email(self,email):
        
        if USER.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists..")
        return email
    
    def validate(self, attrs):

        if attrs['password'] == attrs['confirmPassword']:
            return attrs
        raise serializers.ValidationError('password and confirm password do not match..')
    
    def create(self, validated_data):
        
        user_object = USER(
            email=validated_data['email'],
            first_name = validated_data.get('firstname',''),
            last_name = validated_data.get('lastname','')
        )
        user_object.set_password(validated_data['password'])
        user_object.save()

        _ = Token.objects.create(user=user_object) #creating token for the newly created user

        return validated_data