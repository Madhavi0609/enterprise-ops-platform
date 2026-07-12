from fastapi import FastAPI

from app.routers.organization import router as organization_router
from app.routers.user import router as user_router
from app.routers.department import router as department_router
from app.routers import employee
from app.routers.client import router as client_router
from app.routers.notification import router as notification_router
from app.routers.project import router as project_router

app = FastAPI(
    title="Enterprise Operations Pslatform",
    version="1.0.0",
)

app.include_router(organization_router)
app.include_router(user_router)
app.include_router(department_router)
app.include_router(employee.router)
app.include_router(client_router)
app.include_router(notification_router)
app.include_router(project_router)