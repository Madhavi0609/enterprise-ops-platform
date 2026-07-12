from sqlalchemy.orm import Session

from app.models.document import Document
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate
)


class DocumentRepository:


    @staticmethod
    def create(
        db: Session,
        document: DocumentCreate
    ):

        db_document = Document(
            **document.model_dump()
        )

        db.add(db_document)
        db.commit()
        db.refresh(db_document)

        return db_document



    @staticmethod
    def get_all(db: Session):

        return db.query(Document).all()



    @staticmethod
    def get_by_id(
        db: Session,
        document_id: int
    ):

        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )



    @staticmethod
    def update(
        db: Session,
        document_id: int,
        data: DocumentUpdate
    ):

        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if document:

            for key, value in data.model_dump(
                exclude_unset=True
            ).items():

                setattr(document, key, value)

            db.commit()
            db.refresh(document)

        return document



    @staticmethod
    def delete(
        db: Session,
        document_id: int
    ):

        document = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if document:

            db.delete(document)
            db.commit()

        return document