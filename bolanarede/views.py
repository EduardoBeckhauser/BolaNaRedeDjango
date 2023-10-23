from rest_framework.viewsets import ModelViewSet

from bolanarede.models import Camisa
from bolanarede.serializers import CamisaSerializer

class CamisaViewSet(ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer