from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import Rol, Usuario, Residente, AreaComun, Reserva, Factura, Pago
from .serializers import RolSerializer, UsuarioSerializer, ResidenteSerializer, AreaComunSerializer, ReservaSerializer, FacturaSerializer, PagoSerializer

@extend_schema(tags=['Gestión de roles'])
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

@extend_schema(tags=['Gestión de usuarios'])
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
@extend_schema(tags=['Gestión de residentes'])
class ResidenteViewSet(viewsets.ModelViewSet):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer

@extend_schema(tags=['Gestión de areas'])
class AreaComunViewSet(viewsets.ModelViewSet):
    queryset = AreaComun.objects.all()
    serializer_class = AreaComunSerializer

@extend_schema(tags=['Gestión de reservas'])
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

@extend_schema(tags=['Gestión de facturas'])
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer


@extend_schema(tags=['Gestión de pagos'])
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
