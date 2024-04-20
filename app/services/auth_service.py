# GENERIC LIB
from bson import ObjectId
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
# COLLECTIONS
from app.utils.database import user_collection
# MODEL
# UTILS
from app.utils.config import Config


class AuthService:
    def authenticate_user(username: str, password: str):
        bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        user = user_collection.find_one({'username': username})
        
        if not user:
            return None, {'message':'USER_NOT_FOUND'}
        if not bcrypt_context.verify(password, user.get('password', '')):
            return None, {'message':'WRONG_PASSWORD'}
        return user, None
    
    def create_access_token(username, user_id, user_role, expiration_time = timedelta(minutes=30)):
        payload = {'sub': username, 'id': str(user_id), 'role': user_role}
        expires = datetime.now(timezone.utc) + expiration_time
        payload.update({'exp': expires})
        return jwt.encode(payload, Config.TOKEN.SECRET_KEY, algorithm=Config.TOKEN.ALGORITHM)