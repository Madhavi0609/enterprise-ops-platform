from sqlalchemy.orm import Session

from app.repositories.project import ProjectRepository
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate
)


class ProjectService:


    @staticmethod
    def create(
        db: Session,
        project: ProjectCreate
    ):

        return ProjectRepository.create(
            db,
            project
        )


    @staticmethod
    def get_all(db: Session):

        return ProjectRepository.get_all(db)



    @staticmethod
    def get_by_id(
        db: Session,
        project_id: int
    ):

        return ProjectRepository.get_by_id(
            db,
            project_id
        )



    @staticmethod
    def update(
        db: Session,
        project_id: int,
        data: ProjectUpdate
    ):

        return ProjectRepository.update(
            db,
            project_id,
            data
        )



    @staticmethod
    def delete(
        db: Session,
        project_id: int
    ):

        return ProjectRepository.delete(
            db,
            project_id
        )