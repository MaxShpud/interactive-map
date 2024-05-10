"""3.1

Revision ID: ef196a40a890
Revises: 13461a1379cd
Create Date: 2024-05-10 16:20:04.455443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef196a40a890'
down_revision: Union[str, None] = '13461a1379cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objects', sa.Column('system', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('objects', 'system')
    # ### end Alembic commands ###