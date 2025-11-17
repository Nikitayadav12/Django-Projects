from django.contrib.auth import get_user_model

from rest_framework import  serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id','username','role','password')
        extra_kwargs={'password':{'write_only':True}}


    def create(self, validated_data):
        user=get_user_model().objects.create_user(**validated_data)
        return  user

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()