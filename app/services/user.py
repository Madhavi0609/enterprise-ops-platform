from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all_users(self):
        return self.repository.get_all()

    def get_user(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def create_user(self, user: UserCreate):
        existing_user = self.repository.get_by_email(user.email)

        if existing_user:
            raise ValueError("Email already exists.")

        password_hash = hash_password(user.password)
        return self.repository.create(user, password_hash)

    def update_user(self, user_id: int, user: UserUpdate):
        return self.repository.update(user_id, user)

    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)