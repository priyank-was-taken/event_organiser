from rest_framework import serializers
from . import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Events
        fields = "__all__"


class ReadEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Events
        fields = ["id", "event_image", "event_title", "event_date", "event_category"]


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EventResult
        fields = "__all__"


class ReadResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EventResult
        fields = ["id", "fixture", "team_name1", "team_name2", "team_score1", "team_score2", "result_description",
                  "result_short_description"]


class EventResultSerializer(serializers.ModelSerializer):
    results = ReadResultSerializer(many=True)

    class Meta:
        model = models.Events
        fields = ["id", "event_title", "results"]

