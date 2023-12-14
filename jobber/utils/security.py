from jose import jwt
import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext
from datetime import datetime, timedelta

from services.user_service import get_user_from_json
from models.user_model import UserInDB 


# Initiate a password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "YOUR_SECRET_KEY"  # You should use a separate settings file
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_jwt if decoded_jwt.get("exp") >= datetime.utcnow() else None
    except jwt.PyJWTError:
        return None
    
# Add this to utils/security.py, assuming you have create_access_token and SECRET_KEY as before

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def  get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    print("TOKEN: ", token, flush=True)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD: ", payload, flush=True)
        user_id: str = payload.get("sub")
        print("secondo print", flush=True)
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user_from_json(user_id)
    if user is None:
        raise credentials_exception
    return user