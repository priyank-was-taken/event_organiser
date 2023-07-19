from django.urls import path
from . import views


app_name = "events"

urlpatterns = [
    path("events/<int:pk>/", views.EventsRetrieveAPIView.as_view(), name="single-event"),
    path("events/", views.EventsAPIView.as_view(), name="events"),
    path("result/", views.ResultAPIView.as_view(), name="event-result"),
    path("event-result/", views.EventResultAPIView.as_view(), name="event-result"),
    path("event-result/<int:id>", views.EventResultAPIView.as_view(), name="event-result"),
]
