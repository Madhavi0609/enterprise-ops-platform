from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationUpdate


class NotificationRepository:

    @staticmethod
    def create(
        db: Session,
        notification: NotificationCreate
    ):

        db_notification = Notification(
            **notification.model_dump()
        )

        db.add(db_notification)
        db.commit()
        db.refresh(db_notification)

        return db_notification


    @staticmethod
    def get_all(db: Session):

        return db.query(Notification).all()


    @staticmethod
    def get_by_id(
        db: Session,
        notification_id: int
    ):

        return (
            db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )


    @staticmethod
    def update(
        db: Session,
        notification_id: int,
        data: NotificationUpdate
    ):

        notification = (
            db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )

        if notification:

            for key, value in data.model_dump(
                exclude_unset=True
            ).items():
                setattr(notification, key, value)

            db.commit()
            db.refresh(notification)

        return notification


    @staticmethod
    def delete(
        db: Session,
        notification_id: int
    ):

        notification = (
            db.query(Notification)
            .filter(Notification.id == notification_id)
            .first()
        )

        if notification:
            db.delete(notification)
            db.commit()

        return notification