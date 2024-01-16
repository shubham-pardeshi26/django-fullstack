from django.urls import path,include
from .views import roomView,CreateRoomView
urlpatterns = [
    path('home/', roomView.as_view()),
    path('create-room/', CreateRoomView.as_view()),
]
