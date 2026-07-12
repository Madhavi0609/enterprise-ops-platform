"""update employee salary and hire_date types

Revision ID: 90ac74e7bf18
Revises: acf4c020f63c
Create Date: 2026-07-12 16:36:39.826125

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "90ac74e7bf18"
down_revision: Union[str, Sequence[str], None] = "acf4c020f63c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Change salary from INTEGER to NUMERIC(10,2)
    op.execute("""
        ALTER TABLE employees
        ALTER COLUMN salary
        TYPE NUMERIC(10,2)
        USING salary::NUMERIC(10,2)
    """)

    # Change hire_date from VARCHAR to DATE
    op.execute("""
        ALTER TABLE employees
        ALTER COLUMN hire_date
        TYPE DATE
        USING hire_date::DATE
    """)


def downgrade() -> None:
    # Convert hire_date back to VARCHAR
    op.execute("""
        ALTER TABLE employees
        ALTER COLUMN hire_date
        TYPE VARCHAR(50)
        USING hire_date::VARCHAR
    """)

    # Convert salary back to INTEGER
    op.execute("""
        ALTER TABLE employees
        ALTER COLUMN salary
        TYPE INTEGER
        USING salary::INTEGER
    """)