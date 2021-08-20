from rest_framework import serializers
from app_nfl.models import Team, Schedule
from app_squares.models import Square, Cell
from app_users.models import CustomUser


class NFLSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "teamName",
            "logo",
            "win",
            "loss",
            "draw"
        )
        model = Team

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "date",
            "homeTeam",
            "awayTeam"
        )
        model = Schedule

class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "team_x",
            "team_y",
            "boardStatus"
        )
        model = Square

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "x",
            "y",
            "cellStatus",
            "user"
        )
        model = Cell

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "username",
        )
        model = CustomUser
