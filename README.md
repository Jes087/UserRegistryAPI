# UserRegistryAPI 🚀

A lightweight RESTful API built with **FastAPI** to manage user records using JSON-based storage. Perfect for learning and practicing CRUD operations and RESTful design with Python.

## 🔧 Features

- 📄 Create, Read, Update, Delete (CRUD) user data
- 💡 Built with FastAPI for high performance
- 🗃️ JSON used as a storage layer (no external DB)
- 🧪 Minimalistic, clean structure – great for beginners
- ✅ Fully working and tested locally

## 📁 Tech Stack

- **Python 3.8+**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **JSON file storage**

## 📂 Project Structure

```
├── app.py           # Main FastAPI application
├── database.py      # Database logic using JSON files
├── user_table.json  # Data storage (auto-created if missing)
├── requirements.txt # Python dependencies
```

## ▶️ Running Locally

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FastAPI server
uvicorn app:app --reload
```

Open your browser and go to: [http://localhost:8000/docs](http://localhost:8000/docs) to use the interactive Swagger UI.

## 📬 API Endpoints

| Method | Endpoint     | Description          |
|--------|--------------|----------------------|
| POST   | `/users`     | Add a new user       |
| GET    | `/users`     | Get all users        |
| GET    | `/users/{id}`| Get user by ID       |
| PUT    | `/users/{id}`| Update user by ID    |
| DELETE | `/users/{id}`| Delete user by ID    |

---

## 📘 Learning Outcome

This project helped me understand the **core principles of REST APIs**, including:
- Path parameters
- Request/response models
- CRUD logic separation
- Using JSON for data persistence

---

## 🔗 Author

**Jeswin Jaison**  
[GitHub](http://www.github.com/Jes087) • [LinkedIn](http://www.linkedin.com/in/jeswin-jaison-b2243b255)
