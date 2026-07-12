from sqlalchemy.orm import Session

from app.repositories.client import ClientRepository
from app.schemas.client import ClientCreate


class ClientService:

    @staticmethod
    def create(db: Session, client: ClientCreate):
        return ClientRepository.create(db, client)

    @staticmethod
    def get_all(db: Session):
        return ClientRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, client_id: int):
        return ClientRepository.get_by_id(db, client_id)

    @staticmethod
    def delete(db: Session, client_id: int):
        return ClientRepository.delete(db, client_id)