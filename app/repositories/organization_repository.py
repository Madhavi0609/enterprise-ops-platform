from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


class OrganizationRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Organization).all()

    @staticmethod
    def get_by_id(db: Session, organization_id: int):
        return (
            db.query(Organization)
            .filter(Organization.id == organization_id)
            .first()
        )

    @staticmethod
    def create(db: Session, organization: OrganizationCreate):
        db_organization = Organization(**organization.model_dump())

        db.add(db_organization)
        db.commit()
        db.refresh(db_organization)

        return db_organization

    @staticmethod
    def update(
        db: Session,
        db_organization: Organization,
        organization: OrganizationUpdate,
    ):
        update_data = organization.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_organization, key, value)

        db.commit()
        db.refresh(db_organization)

        return db_organization

    @staticmethod
    def delete(db: Session, db_organization: Organization):
        db.delete(db_organization)
        db.commit()