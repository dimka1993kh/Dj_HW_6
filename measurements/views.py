from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer

class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
