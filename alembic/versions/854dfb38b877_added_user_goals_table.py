"""Added user_goals table

Revision ID: 854dfb38b877
Revises: 0e906e65ac99
Create Date: 2025-05-09 17:00:09.450754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '854dfb38b877'
down_revision: Union[str, None] = '0e906e65ac99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_goals',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('calorie_goal', sa.Float(), nullable=True),
    sa.Column('protein_goal', sa.Float(), nullable=True),
    sa.Column('sugar_goal', sa.Float(), nullable=True),
    sa.Column('fat_goal', sa.Float(), nullable=True),
    sa.Column('carbs_goal', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user_details.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_goals')
    # ### end Alembic commands ###
