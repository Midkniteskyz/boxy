from rest_framework import generics, viewsets

from app_nfl.models import Team, Schedule
from app_squares.models import Square, Cell
from app_users.models import CustomUser
from .serializers import *

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = NFLSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class SquareViewSet(viewsets.ModelViewSet):
    queryset = Square.objects.all()
    serializer_class = SquareSerializer

class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
