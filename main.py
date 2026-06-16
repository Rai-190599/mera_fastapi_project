# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine, text

app = FastAPI()

# PostgreSQL Connection URL
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydb" 

engine = create_engine(DATABASE_URL)

@app.get("/")
def check_db_connection():
    try:
        # DB connection test karne ke liye query
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"message": "DB connected"}
        
    except Exception as e:
        # Debugging ke liye tum terminal me error dekh sakte ho
        print(f"Connection Error: {e}") 
        return {"message": "Failed to connect"}