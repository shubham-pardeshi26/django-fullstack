from django.urls import path, include
from .views import goalView, someGoalView

urlpatterns = [
    path("goal_list/", goalView.as_view()),
    path("some_goal_list/", someGoalView.as_view()),
]
