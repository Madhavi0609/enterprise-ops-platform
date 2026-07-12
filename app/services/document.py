from sqlalchemy.orm import Session

from app.repositories.document import DocumentRepository
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
)


class DocumentService:

    @staticmethod
    def create(
        db: Session,
        document: DocumentCreate,
    ):
        return DocumentRepository.create(
            db,
            document,
        )

    @staticmethod
    def get_all(db: Session):
        return DocumentRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int,
    ):
        return DocumentRepository.get_by_id(
            db,
            document_id,
        )

    @staticmethod
    def update(
        db: Session,
        document_id: int,
        data: DocumentUpdate,
    ):
        return DocumentRepository.update(
            db,
            document_id,
            data,
        )

    @staticmethod
    def delete(
        db: Session,
        document_id: int,
    ):
        return DocumentRepository.delete(
            db,
            document_id,
        )