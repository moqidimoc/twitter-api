"""Create tweets table

Revision ID: 10f023cb7284
Revises: 
Create Date: 2022-06-10 11:53:18.463494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f023cb7284'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=280), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
