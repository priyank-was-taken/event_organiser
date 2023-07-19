from django.db import models
from events.utils import CATEGORY


class Events(models.Model):
    sport_type = models.CharField(choices=CATEGORY, max_length=255, null=True)
    event_image = models.ImageField(upload_to="images", null=True, blank=True)
    event_title = models.CharField(max_length=255, null=True)
    upload_date = models.DateField(auto_now=True)
    event_category = models.CharField(choices=CATEGORY, max_length=255, null=True)
    event_rules = models.TextField(null=True, blank=True)
    event_description = models.CharField(max_length=255, null=True)
    event_trophies = models.ImageField(upload_to="images", null=True, blank=True)
    event_trophies_name = models.CharField(max_length=255, null=True, blank=True)
    event_date = models.DateField(auto_now=False)
    is_upcoming = models.BooleanField(default=True)
    organised_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-pk"]

    def __str__(self):
        return self.event_title


class EventResult(models.Model):
    fixture = models.CharField(max_length=255, null=True, blank=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="results")
    team_name1 = models.CharField(max_length=255, null=True, blank=True)
    team_name2 = models.CharField(max_length=255, null=True, blank=True)
    team_score1 = models.CharField(max_length=255, null=True, blank=True)
    team_score2 = models.CharField(max_length=255, null=True, blank=True)
    result_description = models.CharField(max_length=255, null=True, blank=True)
    result_short_description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Event Result"
        verbose_name_plural = "Event Results"
        ordering = ["-pk"]

    def __str__(self):
        return f"{str(self.team_name1)} | {str(self.team_name1)}"

