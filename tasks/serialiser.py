from rest_framework import serializers
from .models import Task,  Category




class TaskSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"