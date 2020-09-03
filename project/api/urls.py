from django.urls import path, include 
from .views import * 
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('project_users/', ProjectUserListView.as_view()),
    path('project_users/<pk>/', ProjectUserDetailView.as_view()),

]





