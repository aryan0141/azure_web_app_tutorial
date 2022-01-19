from importlib.metadata import requires
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import CustomUser, Resume

class ResumeSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_latest = serializers.BooleanField(default=True, initial=True)
    class Meta:
        model = Resume
        # fields = ('resume_name', 'resume_path', 'is_latest', 'user')
        fields = ('__all__')

    

class CustomUserSerializer(serializers.ModelSerializer):
    resumes = ResumeSerializer(source='resume_set', many=True, read_only=True)
    isDeleted = serializers.HiddenField(default=False)
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'isDeleted', 'resumes')
        # extra_kwargs = {
        #     'password' : {'write_only': True},
        #     'password2' : {'write_only': True},
        # }

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.save()
        return instance

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2')

        extra_kwargs = {
            'password' : {'write_only': True},
            'password2' : {'write_only': True},
        }

    def create(self, data):
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')

        if password == password2:
            user = CustomUser(email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                "error" : "Both passwords do not match"
            })
