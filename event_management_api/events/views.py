from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(organizer=self.request.user)

class EventListCreateView(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticated]

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = [IsAuthenticated]