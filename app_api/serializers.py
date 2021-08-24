from rest_framework import serializers
from app_nfl.models import *
from app_squares.models import *
from app_users.models import *

class NestedCellSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = ('square',"cellstatus","user")

class NFLSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id","teamName","logo","win","loss","draw")
        model = Team

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id","date","homeTeam","awayTeam")
        model = Schedule

class SquareSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id","team_x","team_y","boardStatus")
        model = Square

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id","x","y","cellStatus","user","square")
        model = Cell

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id","username",)
        model = CustomUser
