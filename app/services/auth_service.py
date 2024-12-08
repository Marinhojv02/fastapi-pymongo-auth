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
    def authenticate_user(email: str, password: str, expiration_time = timedelta(minutes=30)):
        bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        user = user_collection.find_one({'email': email})
        
        if not user or not bcrypt_context.verify(password, user.get('password', '')):
            raise HTTPException(status_code=401, detail={'message':'WRONG_USER_OR_PASSWORD'})

        user.get('username', ''), user.get('_id', ''), user.get('role', '')
        
        username = user.get('username', '')
        user_id = user.get('_id', '')
        user_role = user.get('role', '')

        payload = {'sub': username, 'id': str(user_id), 'role': user_role}
        expires = datetime.now(timezone.utc) + expiration_time
        payload.update({'exp': expires})
        return jwt.encode(payload, Config.TOKEN.SECRET_KEY, algorithm=Config.TOKEN.ALGORITHM)