from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """

    class Meta:
        model = User
        fields = ('id', 'username')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """ Add custom claims to payload  """

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
