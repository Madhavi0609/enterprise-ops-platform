from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.notification import (
    NotificationCreate,
    NotificationUpdate,
    NotificationResponse
)

from app.services.notification import NotificationService


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)



@router.post(
    "/",
    response_model=NotificationResponse
)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):

    return NotificationService.create(
        db,
        notification
    )



@router.get(
    "/",
    response_model=list[NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db)
):

    return NotificationService.get_all(db)



@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = NotificationService.get_by_id(
        db,
        notification_id
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification



@router.put(
    "/{notification_id}",
    response_model=NotificationResponse
)
def update_notification(
    notification_id: int,
    data: NotificationUpdate,
    db: Session = Depends(get_db)
):

    notification = NotificationService.update(
        db,
        notification_id,
        data
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification



@router.delete(
    "/{notification_id}"
)
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):

    notification = NotificationService.delete(
        db,
        notification_id
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return {
        "message": "Notification deleted successfully"
    }