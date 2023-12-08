from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

from bolanarede.models import Camisa
from bolanarede.serializers import CamisaSerializer



class CamisaViewSet(ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["time__nome"]
    # search_fields = ["nome"]
    # ordering_fields = ["nome", "preco"]
    # ordering = ["nome"]