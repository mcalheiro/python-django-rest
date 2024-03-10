"""
Validators for client attributes
"""

import re
from validate_docbr import CPF

CPF_PATTERN = CPF()
RG_LEN = 9
PHONE_TEMPLATE = '[0-9]{2} [0-9]{5}-[0-9]{4}'

def nome_valido(nome:str) -> bool:
    return nome.isalpha()

def cpf_valido(cpf:str) -> bool:
    return CPF_PATTERN.validate(cpf)

def rg_valido(rg:str) -> bool:
    return len(rg) == RG_LEN

def celular_valido(celular:str) -> bool:
    return re.findall(PHONE_TEMPLATE, celular)
