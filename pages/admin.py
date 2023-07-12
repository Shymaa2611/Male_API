from django.contrib import admin

from .models import Meal, Rating



class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'user', 'stars']
    list_filter = ['meal', 'user']
    

class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'meal', 'description']
    search_fields = ['meal', 'description']
    list_filter = ['meal', 'description']

admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)