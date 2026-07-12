from fastapi import FastAPI

from app.routers.organization import router as organization_router
from app.routers.user import router as user_router
from app.routers.department import router as department_router
from app.routers import employee


app = FastAPI(
    title="Enterprise Operations Platform",
    version="1.0.0",
)

app.include_router(organization_router)
app.include_router(user_router)
app.include_router(department_router)
app.include_router(employee.router)