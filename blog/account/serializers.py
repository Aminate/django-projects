from rest_framework.serializers import ModelSerializer, CharField, ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserSerializer(ModelSerializer):
    password_confirm = CharField(min_length=7, required=True, write_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confirm')
    def validate(self, attrs):  #validate - отвечает за проверку
        super().validate(attrs)
        password1 = attrs.get('password')
        password2 = attrs.pop('password_confirm')
        if password1 != password2:
            raise ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):   #validated_data - проверенные данные
        return User.objects.create_user(**validated_data)
    

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')