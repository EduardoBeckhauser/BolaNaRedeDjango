from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend


from bolanarede.models import Camisa
from bolanarede.serializers import CamisaSerializer


class CamisaViewSet(ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["time__nome"]