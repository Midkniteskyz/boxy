from django.db import models
from app_users.models import CustomUser
from app_nfl.models import Team

class Square(models.Model):
    team_x = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='teamx')
    team_y = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='teamy')
    boardStatus = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team_x} vs {self.team_y}"

class Cell(models.Model):
    square = models.ForeignKey(Square, on_delete=models.CASCADE, related_name="cells", default=False)
    x = models.IntegerField()
    y = models.IntegerField()
    cellStatus = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=False)

    def __str__(self):
        return self.user
