from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventListCreateView, EventDetailView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('events/', EventListCreateView.as_view(), name='event-list-create'),
  path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
