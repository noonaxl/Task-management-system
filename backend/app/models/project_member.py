from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.db.database import Base

class ProjectMember(Base):
    __tablename__ = "project_members"

    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    role = Column(String, default="member")