from rest_framework import serializers
from .models import Meal,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields=['id','meal','description','no_of_rating','avg_rating']
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['id','user','meal','stars']