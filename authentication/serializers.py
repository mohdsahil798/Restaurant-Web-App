from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id','username', "email",'password', 'mobile_number']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user