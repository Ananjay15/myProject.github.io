from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Registry
from django.http import *
from django.urls import reverse_lazy
from cryptography.fernet import Fernet
import base64


class UserSerialisers(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','phone','email','password','password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self,validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        sample_string = validated_data['password']
        sample_string_bytes = sample_string.encode("ascii")
    
        base64_bytes = base64.b64encode(sample_string_bytes)
        encpass = base64_bytes.decode("ascii")
        
        validate = Registry.objects.create(
            name = validated_data['first_name'] + ' ' + validated_data['last_name'],
            email = validated_data['email'],
            password = encpass,
            phone  = validated_data['phone'],
            is_active = True,
            pending=False
        )
        validate.save()
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({'password':'Passowrd Must match'})
        user.set_password(validated_data['password'])
        user.save()
        return user

