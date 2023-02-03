"""create users example

Revision ID: 69a1b319ce74
Revises: 
Create Date: 2023-01-30 09:02:52.830038

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = "69a1b319ce74"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        text(
            """CREATE TABLE users (
        id BIGINT PRIMARY KEY,
        employee_id VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        user_name VARCHAR(255),
        created_at DATE)"""
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(text("""DROP TABLE users"""))
