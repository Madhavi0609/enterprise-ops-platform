from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)
from app.services.organization_service import OrganizationService


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[OrganizationResponse])
def get_organizations(db: Session = Depends(get_db)):
    return OrganizationService.get_all(db)


@router.get("/{organization_id}", response_model=OrganizationResponse)
def get_organization(organization_id: int, db: Session = Depends(get_db)):
    organization = OrganizationService.get_by_id(db, organization_id)

    if not organization:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return organization


@router.post("/", response_model=OrganizationResponse, status_code=201)
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
):
    return OrganizationService.create(db, organization)


@router.put("/{organization_id}", response_model=OrganizationResponse)
def update_organization(
    organization_id: int,
    organization: OrganizationUpdate,
    db: Session = Depends(get_db),
):
    updated = OrganizationService.update(
        db,
        organization_id,
        organization,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return updated


@router.delete("/{organization_id}")
def delete_organization(
    organization_id: int,
    db: Session = Depends(get_db),
):
    deleted = OrganizationService.delete(db, organization_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return {
        "message": "Organization deleted successfully"
    }