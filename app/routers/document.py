from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse,
)
from app.services.document import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DocumentResponse)
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
):
    return DocumentService.create(db, document)


@router.get("/", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    return DocumentService.get_all(db)


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    document = DocumentService.get_by_id(db, document_id)

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document


@router.put("/{document_id}", response_model=DocumentResponse)
def update_document(
    document_id: int,
    document: DocumentUpdate,
    db: Session = Depends(get_db),
):
    updated = DocumentService.update(
        db,
        document_id,
        document,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return updated


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    deleted = DocumentService.delete(db, document_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return {
        "message": "Document deleted successfully"
    }