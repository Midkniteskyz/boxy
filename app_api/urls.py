from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("teams", TeamsViewSet, basename="teams")
router.register("schedule", ScheduleViewSet, basename="schedule")
router.register("square", SquareViewSet, basename="square")
router.register("cell", CellViewSet, basename="cell")
router.register("user", UserViewSet, basename="user")
# router.register("currentuser", CurrentUserView, basename="currentuser")
# urlpatterns = router.urls

urlpatterns = [
    path('currentuser/', CurrentUserView.as_view())
] + router.urls
