"""empty message

Revision ID: bf0d178bfb04
Revises: 707983673260
Create Date: 2021-02-22 11:34:33.695476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf0d178bfb04'
down_revision = '707983673260'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=150), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('is_complete', sa.Boolean(), nullable=True),
    sa.Column('is_editing', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_due_date'), 'todo', ['due_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_due_date'), table_name='todo')
    op.drop_table('todo')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
