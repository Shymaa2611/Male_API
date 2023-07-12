from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
class Meal(models.Model):
    meal=models.CharField(max_length=20)
    description=models.TextField()
    def __str__(self):
        return self.meal

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)
    stars=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    def __str__(self):
        return str(self.meal.meal)
    class Meta:
        unique_together=(('user','meal'))
        index_together=(('user','meal'))
