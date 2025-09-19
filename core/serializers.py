from rest_framework import serializers
from .models import Rol, Usuario, Residente, AreaComun, Reserva, Factura, Pago,Departamento

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol', 'activo']


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields= ['id','numero','piso','torre']

class ResidenteSerializer(serializers.ModelSerializer):
    usuario_data = UsuarioSerializer(source='usuario', read_only=True)
    departamento_data = DepartamentoSerializer(source='departamento', read_only=True)
    
    class Meta:
        model = Residente
        fields = ['usuario', 'departamento', 'usuario_data', 'departamento_data']
        extra_kwargs = {
            'usuario': {'write_only': True},
            'departamento': {'write_only': True}
        }
        
'''class ResidenteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    departamento = DepartamentoSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), 
        source='usuario', 
        write_only=True
    )
    departamento_id = serializers.PrimaryKeyRelatedField(
        queryset=Departamento.objects.all(), 
        source='departamento', 
        write_only=True
    )
    
    class Meta:
        model = Residente
        fields = ['usuario', 'departamento', 'usuario_id', 'departamento_id']
'''

class AreaComunSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaComun
        fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
