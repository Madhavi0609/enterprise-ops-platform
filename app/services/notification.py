from sqlalchemy.orm import Session

from app.repositories.notification import NotificationRepository
from app.schemas.notification import (
    NotificationCreate,
    NotificationUpdate
)


class NotificationService:


    @staticmethod
    def create(
        db: Session,
        notification: NotificationCreate
    ):

        return NotificationRepository.create(
            db,
            notification
        )


    @staticmethod
    def get_all(db: Session):

        return NotificationRepository.get_all(db)


    @staticmethod
    def get_by_id(
        db: Session,
        notification_id: int
    ):

        return NotificationRepository.get_by_id(
            db,
            notification_id
        )


    @staticmethod
    def update(
        db: Session,
        notification_id: int,
        data: NotificationUpdate
    ):

        return NotificationRepository.update(
            db,
            notification_id,
            data
        )


    @staticmethod
    def delete(
        db: Session,
        notification_id: int
    ):

        return NotificationRepository.delete(
            db,
            notification_id
        )