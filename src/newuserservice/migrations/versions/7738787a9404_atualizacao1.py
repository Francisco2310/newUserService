"""atualizacao1

Revision ID: 7738787a9404
Revises: 
Create Date: 2025-03-02 03:08:20.244564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7738787a9404'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=100), nullable=False),
    sa.Column('criado_em', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
