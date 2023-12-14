from uuid import UUID

from fastapi import APIRouter, status, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from databases.models import User as DBUser
from utils.security import create_access_token, get_current_user, get_password_hash, verify_password
from models.user_model import UserCreate, User
from services.user_service import UserService

router = APIRouter()

user_service = UserService()

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate):
    hashed_password = get_password_hash(user_create.password)
    user_in_db = await user_service.create_user(user_create, hashed_password)
    return User(**user_in_db.dict())


#@router.post("/users/login")
#def login_for_access_token(username: str, password: str, db: Session = Depends(get_db)):
#    user = db.query(DBUser).filter(DBUser.username == username).first()
#    if not user or not verify_password(password, user.hashed_password):
#        raise HTTPException(
#            status_code=status.HTTP_401_UNAUTHORIZED,
#            detail="Incorrect username or password",
#            headers={"WWW-Authenticate": "Bearer"},
#        )
#    access_token = create_access_token(data={"sub": user.id})
#    return {"access_token": access_token, "token_type": "bearer"}

#@router.get("/users/{user_id}", response_model=User)
#def get_user(user_id: UUID, current_user: User = Security(get_current_user), db: Session = Depends(get_db)):
#    user_data = db.query(DBUser).filter(DBUser.id == str(user_id)).first()
#    if not user_data:
#        raise HTTPException(status_code=404, detail="User not found")
#    return User(**user_data.dict())