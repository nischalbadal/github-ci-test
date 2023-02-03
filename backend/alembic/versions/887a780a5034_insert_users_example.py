"""insert users example

Revision ID: 887a780a5034
Revises: 69a1b319ce74
Create Date: 2023-01-31 12:05:12.861355

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = "887a780a5034"
down_revision = "69a1b319ce74"
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        text(
            """INSERT INTO users VALUES ('1', '1', 'TEST', 'TEST', 'test@test.com', 'drowssap', 'test', '2022-01-31'),
                                            ('2', '2', 'TesT', 'TesT', 'test@test.com', 'DrowssaP', 'test2', '2022-01-31')"""
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(text("""DELETE FROM users"""))
