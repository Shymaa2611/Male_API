from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Rating,Meal
from .serializers import MealSerializers,RatingSerializers,UserSerializers
from rest_framework.decorators import action
import rest_framework.status as status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

class MealViewSet(viewsets.ModelViewSet):
   queryset=Meal.objects.all()
   serializer_class=MealSerializers
   authentication_classes=(TokenAuthentication,)
   permission_classes=(IsAuthenticated,)
   @action(methods=['POST'],detail=True)
   def meal_rate(self, request, pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            #username = request.data['username']
            #user = User.objects.get(username=username)
            user=request.user

            try:
                rating = Rating.objects.get(user=user.id, meal=meal.id) 
                rating.stars = stars
                rating.save()
                serializer = RatingSerializers(rating, many=False)
                json = {
                    'message': 'Meal Rate is Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_201_CREATED)

            except:
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer=RatingSerializers(rating, many=False)
                json = {
                    'message': 'Meal Rate is Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

        else:
            json = {
                'message': 'is not valid'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializers
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)