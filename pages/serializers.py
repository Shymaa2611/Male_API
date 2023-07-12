from rest_framework import serializers
from .models import Meal,Rating
from django.contrib.auth.models import User
class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields=['id','meal','description']
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['id','user','meal','stars']