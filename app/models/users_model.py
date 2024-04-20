from pydantic import BaseModel

class User(BaseModel):
    nome: str
    cpf: str
    username: str
    password: str
    email: str
    celular: str
    funcao: str
    
class CreateUserPayload(BaseModel):
    name: str
    cpf: str
    username: str
    password: str
    email: str
    phone: str