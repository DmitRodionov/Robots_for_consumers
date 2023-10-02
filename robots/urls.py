from django.urls import path
from . import views

urlpatterns = [
    path('api/create_robot/', views.CreateRobotView.as_view(), name='create-robot'),
]
