from django.urls import path, include
from .views import  TaskView ,  CategoryView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'tasks')
router.register(r'categories', CategoryView )

urlpatterns = [
    path('', include(router.urls))
]