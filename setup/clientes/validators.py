"""
Validators for client attributes
"""

CPF_LEN = 11
RG_LEN = 9
PHONE_LEN = 11

def nome_valido(nome:str) -> bool:
    return nome.isalpha()

def cpf_valido(cpf:str) -> bool:
    return len(cpf) == CPF_LEN

def rg_valido(rg:str) -> bool:
    return len(rg) == RG_LEN

def celular_valido(celular:str) -> bool:
    return len(celular) >= PHONE_LEN
