from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UsuarioViewSet, ResidenteViewSet, AreaComunViewSet, ReservaViewSet, FacturaViewSet, PagoViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'residentes', ResidenteViewSet)
router.register(r'areas', AreaComunViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
