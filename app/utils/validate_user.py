# GENERIC LIB
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
# COLLECTIONS
# MODEL
# UTILS
from app.utils.config import Config


def get_current_user(token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl='/auth/login'))]):
    try:
        payload = jwt.decode(token, Config.TOKEN.SECRET_KEY, algorithms=Config.TOKEN.ALGORITHM)
        username: str = payload.get('sub')
        user_id: str = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="COULD_NOT_VALIDATE")
        return {'username':username ,'user_id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="COULD_NOT_VALIDATE")