from rest_framework import serializers
from .models import User, Category, Training, UserTraining

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'phone_number', 'password', 'confirm_password', 'role']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password dan Confirm Password tidak sama")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email', 'phone_number', 'role']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TrainingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Training
        fields = ['id', 'title', 'instructor', 'category', 'price']
        
class UserTrainingSerializer(serializers.ModelSerializer):
    training = TrainingSerializer()
    class Meta:
        model = UserTraining
        fields = ['id', 'training', 'purchased_at']

