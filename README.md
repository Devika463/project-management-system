# Project Management System

## Overview

A Project Management System built using FastAPI, PostgreSQL, SQLAlchemy, Alembic, and JWT Authentication.

The system allows organizations to manage users, projects, and tasks while supporting authentication, filtering, pagination, validation, and database migrations.

---

## Tech Stack

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Passlib (Password Hashing)

### Database

* PostgreSQL

---

## Project Structure

```text
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── main.py
│   └── test_db.py
├── migrations/
├── alembic.ini
├── requirements.txt
├── .env
└── .env.example
```

---

## Architecture

The application follows a layered architecture:

### API Layer

Handles HTTP requests and responses.

### Schema Layer

Pydantic models for validation and serialization.

### Repository Layer

Handles database operations.

### Model Layer

SQLAlchemy ORM models.

### Core Layer

Authentication, security, configuration, and database setup.

### Service Layer

Business logic and reusable services.

---

## Database Design

### Users

* id
* name
* email
* role

### Projects

* id
* name
* description
* created_by

### Tasks

* id
* title
* description
* status
* project_id
* assigned_to
* due_date

---

## ER Diagram

![ER Diagram](docs/er-diagram.png)

---

## Authentication

JWT-based authentication is implemented.

### Login Endpoint

POST /auth/login

Returns:

* access_token
* token_type

Protected routes require a valid JWT token.

---

## API Endpoints

### Users

* POST /users/
* GET /users/

### Projects

* POST /projects/
* GET /projects/
* PUT /projects/{id}
* DELETE /projects/{id}

### Tasks

* POST /tasks/
* GET /tasks/
* PATCH /tasks/{id}/assign
* PATCH /tasks/{id}/status

---

## Features

* JWT Authentication
* CRUD Operations
* Task Assignment
* Task Status Updates
* Filtering
* Pagination
* Validation
* Error Handling
* Alembic Migrations
* Swagger Documentation

---

## Environment Variables

Create a .env file:

DATABASE_URL=postgresql://postgres:password@localhost:5432/project_management

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

---

## Setup Instructions

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
alembic upgrade head
```

### Start Application

```bash
uvicorn app.main:app --reload
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Database Migrations

Create migration:

```bash
alembic revision --autogenerate -m "message"
```

Apply migration:

```bash
alembic upgrade head
```

---

## Future Improvements

* Role-Based Access Control
* Docker Support
* Unit Testing
* Frontend Dashboard Enhancements
