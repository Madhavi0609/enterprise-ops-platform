from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()

    def get_by_id(self, user_id: int):
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_by_email(self, email: str):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def create(self, user: UserCreate, password_hash: str):

        db_user = User(
            username=user.username,
            email=user.email,
            password_hash=password_hash,
            role=user.role
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def update(self, user_id: int, user):

        db_user = self.get_by_id(user_id)

        if not db_user:
            return None

        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)

        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def delete(self, user_id: int):

        db_user = self.get_by_id(user_id)

        if not db_user:
            return None

        self.db.delete(db_user)
        self.db.commit()

        return db_user