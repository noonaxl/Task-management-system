from fastapi import FastAPI
from backend.app.routers.user import router as user_router
from backend.app.db.database import Base, engine
from backend.app.models import user, project, task, project_member, task_history
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)