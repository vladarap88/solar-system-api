"""empty message

Revision ID: fcb077a5ff81
Revises: 578fcb6c6536
Create Date: 2024-10-31 12:35:53.102059

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fcb077a5ff81"
down_revision = "578fcb6c6536"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "planet",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("distance_from_sun", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("planet")
    # ### end Alembic commands ###
