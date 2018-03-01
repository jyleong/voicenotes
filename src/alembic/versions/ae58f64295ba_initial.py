"""initial

Revision ID: ae58f64295ba
Revises: 
Create Date: 2018-02-11 15:22:17.659140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae58f64295ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('messages',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('messageContent', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('messages')
    pass
