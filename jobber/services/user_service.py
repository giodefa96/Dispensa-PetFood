from models.user_model import UserInDB
form models import User
from .database import Database



class UserService:
    def __init__(self, database: Database = Database()):
        self.db = database.SessionLocal()

    #def get_user(self, user_id: int):
    #    return self.db.query(User.User).filter(User.User.id == user_id).first()

    async def create_user(self, user: UserInDB, hashed_password: str):
        models = User()
        db_user = models.User(username=user.username, hashed_password=hashed_password, email=user.email)
        
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user
