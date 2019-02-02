"""empty message

Revision ID: 4924f4bbbb9a
Revises: 
Create Date: 2019-02-02 10:58:42.843664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4924f4bbbb9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('college',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('app_deadline', sa.String(), nullable=True),
    sa.Column('rec_deadline', sa.String(), nullable=True),
    sa.Column('num_essays', sa.String(), nullable=True),
    sa.Column('midyear_report', sa.String(), nullable=True),
    sa.Column('acceptance_rate', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('college')
    # ### end Alembic commands ###