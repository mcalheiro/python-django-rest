from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    """
    Lista todos os clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
