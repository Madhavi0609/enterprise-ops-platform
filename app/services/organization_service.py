from sqlalchemy.orm import Session

from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


class OrganizationService:

    @staticmethod
    def get_all(db: Session):
        return OrganizationRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, organization_id: int):
        return OrganizationRepository.get_by_id(db, organization_id)

    @staticmethod
    def create(db: Session, organization: OrganizationCreate):
        return OrganizationRepository.create(db, organization)

    @staticmethod
    def update(
        db: Session,
        organization_id: int,
        organization: OrganizationUpdate,
    ):
        db_organization = OrganizationRepository.get_by_id(
            db,
            organization_id,
        )

        if not db_organization:
            return None

        return OrganizationRepository.update(
            db,
            db_organization,
            organization,
        )

    @staticmethod
    def delete(db: Session, organization_id: int):
        db_organization = OrganizationRepository.get_by_id(
            db,
            organization_id,
        )

        if not db_organization:
            return False

        OrganizationRepository.delete(
            db,
            db_organization,
        )

        return True