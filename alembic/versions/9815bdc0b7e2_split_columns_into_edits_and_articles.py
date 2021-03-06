"""split columns into edits and articles.

Revision ID: 9815bdc0b7e2
Revises: 109b92e34c6d
Create Date: 2020-04-17 09:57:08.714751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9815bdc0b7e2'
down_revision = '109b92e34c6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.drop_column('article', 'is_ready_for_release')
    op.drop_column('article', 'preview')
    op.drop_column('article', 'edited')
    op.drop_column('article', 'article_id')
    op.drop_column('article', 'is_edited')
    op.drop_column('article', 'title')
    op.drop_column('article', 'user_id')
    op.drop_column('article', 'content')
    op.add_column('user', sa.Column('authorization_level', sa.Integer(), nullable=True))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=20), nullable=False))
    op.drop_column('user', 'authorization_level')
    op.add_column('article', sa.Column('content', sa.TEXT(), nullable=False))
    op.add_column('article', sa.Column('user_id', sa.INTEGER(), nullable=False))
    op.add_column('article', sa.Column('title', sa.VARCHAR(length=100), nullable=False))
    op.add_column('article', sa.Column('is_edited', sa.BOOLEAN(), nullable=True))
    op.add_column('article', sa.Column('article_id', sa.INTEGER(), nullable=False))
    op.add_column('article', sa.Column('edited', sa.DATETIME(), nullable=True))
    op.add_column('article', sa.Column('preview', sa.VARCHAR(length=200), nullable=False))
    op.add_column('article', sa.Column('is_ready_for_release', sa.BOOLEAN(), nullable=True))
    op.create_foreign_key(None, 'article', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
