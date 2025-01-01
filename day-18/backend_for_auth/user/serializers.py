from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser
from django.core.validators import FileExtensionValidator
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    cover_photo = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'bio', 'cover_photo', 'id_number')

    def validate(self, attrs):
        # Check password confirmation
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Validate cover photo size if provided
        cover_photo = attrs.get('cover_photo')
        if cover_photo and cover_photo.size > 1024 * 1024:
            raise serializers.ValidationError({"cover_photo": "The file size must be less than 1 MB."})

        return attrs

    def create(self, validated_data):
        # Remove the password confirmation field
        validated_data.pop('password2')

        # Create the user with hashed password
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            id_number=validated_data['id_number'],
            cover_photo=validated_data.get('cover_photo', None),
        )
        user.set_password(validated_data['password'])
        user.save()
        print("User created with username: %s", user.username)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ("password","is_superuser","is_staff","is_active","groups")
        # fields = '__all__'

    def to_internal_value(self, data):
        cleaned_data = {}
        for key, value in data.items():
            if isinstance(value, bytes):
                cleaned_data[key] = value.decode('utf-8', errors='replace')
            else:
                cleaned_data[key] = value
        return super().to_internal_value(cleaned_data)