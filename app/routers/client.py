from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.client import ClientCreate, ClientResponse
from app.services.client import ClientService

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return ClientService.create(db, client)


@router.get("/", response_model=list[ClientResponse])
def get_clients(db: Session = Depends(get_db)):
    return ClientService.get_all(db)


@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return ClientService.get_by_id(db, client_id)


@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    ClientService.delete(db, client_id)
    return {"message": "Client deleted successfully"}