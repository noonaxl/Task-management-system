from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from backend.app.db.database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

    is_archived = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)