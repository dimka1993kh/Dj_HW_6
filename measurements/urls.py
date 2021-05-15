from rest_framework import routers
from .views import ProjectViewSet, MeasurementViewSet
from django.urls import path, include

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

router = routers.DefaultRouter()
router.register("measurement", MeasurementViewSet, basename="measurement")
router.register("project", ProjectViewSet, basename="project")


urlpatterns = router.urls