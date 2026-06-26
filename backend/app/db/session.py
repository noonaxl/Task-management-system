from backend.app.db.database import SessionLocal

# создаём сессию на каждый запрос
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()