"""2

Revision ID: 13461a1379cd
Revises: d83e40b451ad
Create Date: 2024-04-30 15:27:28.468189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13461a1379cd'
down_revision: Union[str, None] = 'd83e40b451ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('system', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('routes_objects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['object_id'], ['objects.id'], ),
    sa.ForeignKeyConstraint(['route_id'], ['routes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routes_objects')
    op.drop_table('routes')
    # ### end Alembic commands ###