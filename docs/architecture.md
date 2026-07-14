# Enterprise Operations Platform Architecture

## Architecture

The application follows a layered architecture:

- Routers → Handle HTTP requests
- Services → Business logic
- Repositories → Database operations
- Models → SQLAlchemy ORM entities
- Schemas → Pydantic request/response validation
- Core → Database configuration, security, and JWT authentication

## Authentication

- JWT Access Token
- JWT Refresh Token
- Password hashing using bcrypt
- Role-based authorization

## Database

PostgreSQL with Alembic migrations.

## API Documentation

Available at:

- /docs
- /openapi.json