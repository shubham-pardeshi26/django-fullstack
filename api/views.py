from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializer import RoomSerializer


class roomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class getRoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer