from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import nome_valido, cpf_valido, rg_valido, celular_valido
from clientes.validators import CPF_LEN, RG_LEN

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome nao deve possuir digitos'})

        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':f'O CPF deve possuir {CPF_LEN} digitos'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':f'O RG deve possuir {RG_LEN} digitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'Numero de celular invalido. Utilize o seguinte padrao: ## #####-####'})

        return data
