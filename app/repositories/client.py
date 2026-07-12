from sqlalchemy.orm import Session

from app.models.client import Client
from app.schemas.client import ClientCreate


class ClientRepository:

    @staticmethod
    def create(db: Session, client: ClientCreate):
        db_client = Client(**client.model_dump())

        db.add(db_client)
        db.commit()
        db.refresh(db_client)

        return db_client

    @staticmethod
    def get_all(db: Session):
        return db.query(Client).all()

    @staticmethod
    def get_by_id(db: Session, client_id: int):
        return db.query(Client).filter(Client.id == client_id).first()

    @staticmethod
    def delete(db: Session, client_id: int):
        client = db.query(Client).filter(Client.id == client_id).first()

        if client:
            db.delete(client)
            db.commit()

        return client