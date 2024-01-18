from django.shortcuts import render
from rest_framework import generics, status
from .models import GoalListModel
from .serializer import AllGoalSerializer, SomeGoalSerializer


# Create your views here.
class goalView(generics.ListCreateAPIView):
    queryset = GoalListModel.objects.all()
    serializer_class = AllGoalSerializer


class someGoalView(generics.ListAPIView):
    queryset = GoalListModel.objects.filter(goal_status="in_queue")
    serializer_class = SomeGoalSerializer


