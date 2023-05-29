"""initial_migration

Revision ID: 1974fc8cb77e
Revises: 
Create Date: 2023-05-24 12:02:31.260372

"""
import arrow
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1974fc8cb77e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    user_table = op.create_table('user',
                                 sa.Column('id', sa.String(), nullable=False),
                                 sa.Column('name', sa.String(length=50), nullable=False),
                                 sa.Column('email', sa.String(), nullable=False),
                                 sa.Column('password', sa.String(length=255), nullable=False),
                                 sa.Column('created_at', sa.DateTime(), nullable=False),
                                 sa.Column('updated_at', sa.DateTime(), nullable=True),
                                 sa.PrimaryKeyConstraint('id')
                                 )

    op.bulk_insert(user_table, [
        {"id": "1231ae1e-6b41-4dd1-89bf-ac144e8b2a1d", "name": "Urich", "email": "oliveira.urich@gmail.com",
         "password": "$2b$12$webTBMd4My.fP96k1iaXMenkQkxoX/Eenk0vYdRBVfVT32tBmEFZ.",
         "created_at": str(arrow.now())}
    ])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
