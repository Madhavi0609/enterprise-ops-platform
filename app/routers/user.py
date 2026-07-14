from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user import UserService
from app.auth.dependencies import (
    get_current_user,
    role_required
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(
        role_required(["Admin"])
    )
):
    service = UserService(db)

    return service.get_all_users()



@router.get(
    "/me",
    response_model=UserResponse
)
def me(
    current_user=Depends(get_current_user)
):
    return current_user



@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        role_required(["Admin"])
    )
):

    service = UserService(db)

    user = service.get_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user



@router.post(
    "/",
    response_model=UserResponse
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        role_required(["Admin"])
    )
):

    service = UserService(db)

    try:
        return service.create_user(user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )



@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(
        role_required(["Admin"])
    )
):

    service = UserService(db)

    updated_user = service.update_user(
        user_id,
        user
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user



@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        role_required(["Admin"])
    )
):

    service = UserService(db)

    deleted_user = service.delete_user(
        user_id
    )

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }