from rest_framework import views, permissions, generics, viewsets, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import serializers, models


class ListRetrieveView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class EventsAPIView(generics.ListAPIView):
    queryset = models.Events.objects.all()
    serializer_class = serializers.ReadEventSerializer


class EventsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventSerializer


class ResultAPIView(generics.ListAPIView):
    queryset = models.EventResult.objects.all()
    serializer_class = serializers.ResultSerializer


class EventResultAPIView(generics.ListAPIView):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventResultSerializer


class EventResultRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Events.objects.all()
    serializer_class = serializers.EventResultSerializer





