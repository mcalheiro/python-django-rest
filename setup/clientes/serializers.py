from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_nome(self, nome:str) -> str:
        if not nome.isalpha():
            raise serializers.ValidationError('O nome nao deve ter digitos')
        return nome

    def validate_cpf(self, cpf:str) -> str:
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve ter 11 digitos')
        return cpf

    def validate_rg(self, rg:str) -> str:
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve ter 9 digitos')
        return rg
    
    def validate_celular(self, celular:str) -> str:
        if len(celular) < 11:
            raise serializers.ValidationError('O celular deve ter pelo menos 11 digitos')
        return celular
