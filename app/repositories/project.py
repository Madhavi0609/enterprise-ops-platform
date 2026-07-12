from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectRepository:


    @staticmethod
    def create(
        db: Session,
        project: ProjectCreate
    ):

        db_project = Project(
            **project.model_dump()
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)

        return db_project



    @staticmethod
    def get_all(db: Session):

        return db.query(Project).all()



    @staticmethod
    def get_by_id(
        db: Session,
        project_id: int
    ):

        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )



    @staticmethod
    def update(
        db: Session,
        project_id: int,
        data: ProjectUpdate
    ):

        project = (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if project:

            for key, value in data.model_dump(
                exclude_unset=True
            ).items():

                setattr(project, key, value)

            db.commit()
            db.refresh(project)

        return project



    @staticmethod
    def delete(
        db: Session,
        project_id: int
    ):

        project = (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if project:

            db.delete(project)
            db.commit()

        return project