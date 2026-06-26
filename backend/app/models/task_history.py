from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from backend.app.db.database import Base
from datetime import datetime

class TaskHistory(Base):
    __tablename__ = "task_history"

    id = Column(Integer, primary_key=True, index=True)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    changed_by = Column(Integer, ForeignKey("users.id"))

    field_name = Column(String)
    old_value = Column(String)
    new_value = Column(String)

    changed_at = Column(DateTime, default=datetime.utcnow)