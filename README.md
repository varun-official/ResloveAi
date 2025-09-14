# ResolveAI

A FastAPI-based application for user management with MongoDB and Beanie ODM.

## Features

- User CRUD operations
- Skill-based filtering with regex support
- MongoDB integration via Beanie
- Async endpoints

## Folder Structure

```
app/
  ├── config/         # Database and app config
  ├── models/         # Beanie document models
  ├── routers/        # API route definitions
  ├── schemas/        # Pydantic schemas
  └── service/        # Business logic/services
main.py               # FastAPI entry point
requirements.txt       # Python dependencies
.env                   # Environment variables
```

## Setup

1. Clone the repo:
   ```sh
   git clone https://github.com/varun-official/ResloveAi.git
   cd ResloveAi
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your `.env` file:
   ```env
   MONGODB_URI=mongodb://localhost:27017/beanie_db
   ```
5. Run the app:
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /users/` — Add user
- `GET /users/` — List users (supports skill regex filtering)
- `PUT /users/{email}` — Update user
- `DELETE /users/{email}` — Delete user

## License

MIT
