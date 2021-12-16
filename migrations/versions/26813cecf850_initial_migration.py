"""Initial migration

Revision ID: 26813cecf850
Revises: 
Create Date: 2021-12-13 23:32:50.169511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26813cecf850'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('header', sa.String(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=False),
    sa.Column('is_link_access', sa.Boolean(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('header')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('registration_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###

    sql_cache = open("db_cache/flask_blog_public_posts.sql")
    from services.logger_service import main_logger
    main_logger.info("-----SEEDING INIT DB DATA!")
    main_logger.info(sql_cache.read())
    op.execute(sql_cache.read())

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('posts')
    # ### end Alembic commands ###
