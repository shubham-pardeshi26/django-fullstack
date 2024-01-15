from django.urls import path,include
from .views import roomView,getRoomView
urlpatterns = [
    path('home/', roomView.as_view()),
    path('getRoomDetails/', getRoomView.as_view()),
]
