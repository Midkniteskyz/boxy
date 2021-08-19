from rest_framework import generics

from app_nfl import models
from app_squares import models
from app_users import models
from .serializers import *

class ListTeams(generics.ListCreateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = NFLSerializer


class DetailTeam(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Team.objects.all
    serializer_class = NFLSerializer
