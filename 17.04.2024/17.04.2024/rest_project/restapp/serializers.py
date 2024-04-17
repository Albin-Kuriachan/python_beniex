
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role
from rest_framework_simplejwt.tokens import RefreshToken



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name',  'email','password' )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role', 'user']

class Updateserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name',  'email' )



class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()


    def get_refresh_token(self, instance):
        refresh_token = RefreshToken.for_user(instance)
        return str(refresh_token)

    def get_access_token(self, instance):
        refresh_token = RefreshToken.for_user(instance)
        return str(refresh_token.access_token)






   

