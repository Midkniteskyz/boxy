from django.db import models
from django.utils import timezone

class Team(models.Model):
    teamName = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="nfl/teamlogos/", default=None)
    win = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)

    def __str__(self):
        return self.teamName

class Schedule(models.Model):
    date = models.DateTimeField()
    awayTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='awayTeam')
    homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='homeTeam')

    def __str__(self):
        return f"{self.homeTeam} vs {self.awayTeam} @{self.date}"
