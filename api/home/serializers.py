from rest_framework import serializers
from home.models import (
    Banner
)
from administration.models import User



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password','contact']

    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
    

    def validate(self, attrs):
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user