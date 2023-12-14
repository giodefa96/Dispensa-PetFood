import uvicorn
from fastapi import FastAPI

# Import routers
from controllers.user_controller import router as user_router

# Import database stuff (depending on how you have organized it)
from databases.database import engine
import databases.models

# Creating database tables
# Depending on your ORM and migration tool, the method may differ.
# The following is how you might do it with SQLAlchemy and Alembic.
databases.models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include your routes
app.include_router(user_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)