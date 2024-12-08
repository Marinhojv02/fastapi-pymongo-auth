from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re

class User(BaseModel):
    name: str
    cpf: str
    username: str
    email: EmailStr
    phone: str
    role: str

    @validator("cpf")
    def validate_cpf(cls, value):
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', value)
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve ter 11 dígitos numéricos")
        
        # Validação do CPF com algoritmos oficiais
        if not cls.is_valid_cpf(cpf):
            raise ValueError("CPF inválido")
        
        return cpf

    @staticmethod
    def is_valid_cpf(cpf: str) -> bool:
        """Validação oficial do CPF"""
        if len(set(cpf)) == 1:
            return False
        
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                return False
        return True

    @validator("phone")
    def validate_celular(cls, value):
        # Regex para validar o formato brasileiro de celular
        pattern = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
        if not re.match(pattern, value):
            raise ValueError("Celular deve estar no formato (XX)XXXXX-XXXX ou similar")
        return value


class CreateUserPayload(BaseModel):
    name: str
    cpf: str
    username: str
    password: str
    email: EmailStr
    phone: str

    @validator("cpf")
    def validate_cpf(cls, value):
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', value)
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve ter 11 dígitos numéricos")
        
        # Validação do CPF com algoritmos oficiais
        if not cls.is_valid_cpf(cpf):
            raise ValueError("CPF inválido")
        
        return cpf

    @staticmethod
    def is_valid_cpf(cpf: str) -> bool:
        """Validação oficial do CPF"""
        if len(set(cpf)) == 1:
            return False
        
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                return False
        return True

    @validator("phone")
    def validate_phone(cls, value):
        # Regex para validar o formato brasileiro de celular
        pattern = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
        if not re.match(pattern, value):
            raise ValueError("Telefone deve estar no formato (XX)XXXXX-XXXX ou similar")
        return value

class UpdateUserPayload(BaseModel):
    name: Optional[str] = None
    cpf: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    @validator("phone")
    def validate_phone(cls, value):
        pattern = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'  # Regex para formato brasileiro
        if not re.match(pattern, value):
            raise ValueError("Telefone deve estar no formato (XX)XXXXX-XXXX ou similar")
        return value