# mera_fastapi_project
🛠️ Prerequisites
Before running this project, ensure you have the following installed:

Python 3.8+

Docker & Docker Desktop

Git

🚀 Setup & Installation
Follow these steps to set up the project locally:

Step 1: Clone or Create the Project Directory
Bash


mkdir mera_fastapi_project
cd mera_fastapi_project
Step 2: Set up a Virtual Environment
Bash


# Create virtual environment
```python -m venv venv```

# Activate virtual environment
# On Windows:
```venv\\Scripts\\activate```
# On Mac/Linux:
```source venv/bin/activate```

Step 3: Install Dependencies
Make sure your requirements.txt is updated, then run:

```Bash

pip install -r requirements.txt

```

🐳 Running the Application
Step 1: Start the PostgreSQL Database (Docker)
Ensure Docker Desktop is running, then spin up the database container:

```Bash


docker compose up -d

```
Step 2: Run the FastAPI Server
Start the development server using Uvicorn:

```Bash


uvicorn main:app --reload

```
The server will be live at http://127.0.0.1:8000/.

🧪 Testing the Database "Down" Scenario
To verify that the API correctly returns a failure response when the database is unavailable:

Check Active Connection: Visit http://127.0.0.1:8000/ in your browser. You should see:

JSON


{ "message": "DB connected" }
Stop the Database Container: Run the following command in your terminal:

```Bash


docker stop fastapi_postgres_db

```
Verify Fail Response: Refresh http://127.0.0.1:8000/. You should now see:

JSON


{ "message": "Failed to connect" }
Restart the Database: To restore the connection, run:

```Bash


docker start fastapi_postgres_db

```