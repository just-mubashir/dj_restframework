from django.db import models
from rest_framework import serializers

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.FloatField()
    auhor = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields ="__all__"