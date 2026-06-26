from backend.app.db.database import SessionLocal

def test_db_connection():
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        print("DB connection OK")
    except Exception as e:
        print("DB connection FAILED:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()