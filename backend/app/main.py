from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.users import router as user_router
from app.api.auth import router as auth_router
from app.api.projects import router as project_router
from app.api.tasks import router as task_router

app = FastAPI(
    title="Project Management API"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(project_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {
        "message": "Project Management API"
    }