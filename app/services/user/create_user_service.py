# GENERIC LIB
from passlib.context import CryptContext
# COLLECTIONS
from app.utils.database import user_collection
# MODEL
from app.pydantic_models.users_model import CreateUserPayload
# UTILS
from app.utils.validate_email import ValidateEmail
from app.utils.validate_phone_number import ValidatePhoneNumber

class CreateUserService:
    def __init__(self, user_info:CreateUserPayload, role:str = 'CLIENT'):
        self.role = role
        self.name = user_info.name
        self.cpf = user_info.cpf
        self.username = user_info.username
        self.password = user_info.password
        self.email = user_info.email
        self.phone = user_info.phone
        
    def validate_phone_number(self):
        formated_phone = ValidatePhoneNumber(self.phone)
        self.phone = formated_phone.format_numero(self.phone)
    
    def validate_email(self):
        return ValidateEmail(self.email)
    
    def check_repeated_user(self):
        user = user_collection.find_one({
            '$or':[
                {'username': self.username},
                {'cpf': self.cpf},
                {'email': self.email},
                {'phone': self.phone},
            ]
        })

        if user:
            raise Exception('USER_ALREADY_EXISTS')
        return
    
    def hash_password(self):
        bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        hashed_password = bcrypt_context.hash(self.password)
        self.hashed_password = hashed_password

    def create(self):
        self.validate_email()
        self.validate_phone_number()
        self.check_repeated_user()
        self.hash_password()
        
        new_user = {
            'username': self.username,
            'email': self.email,
            'password': self.hashed_password,
            'name':self.name,
            'cpf':self.cpf,
            'phone':self.phone,
            'role': self.role,
            'is_active': True,
        }
        user_collection.insert_one(new_user)            
        return new_user