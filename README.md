Coza Store 
- Coza Store is a **FastAPI-based Web Application** that simulates an e-commerce store.  
- It includes **user authentication, product showcase, and SQLite database integration**.  


Technologies Used
- **Backend** → Python (FastAPI)  
- **Server** → Uvicorn  
- **Database** → SQLite (`users.db`)  
- **Frontend** → HTML, CSS, JavaScript (in `static/`), Bootstrap, JQuery




1. First Of all Install Requirements
    - pip install -r requirements.txt


2. Run the FastAPI App
   - uvicorn main:app --reload

3. Access the App

  Application will run at:
    - http://127.0.0.1:8000/
  
  FastAPI API Documentation is available at:
    - http://127.0.0.1:8000/docs

4. Open the database
   - sqlite3 users.db

     4.1 List all tables
       - .tables
         
         - This will show tables:
                  contacts   users

      4.2 Show all data from contacts table
       - SELECT * FROM contacts;

      4.3 Show all data from users table
       - SELECT * FROM users;

      4.4 Exit SQLite
       - .exit

