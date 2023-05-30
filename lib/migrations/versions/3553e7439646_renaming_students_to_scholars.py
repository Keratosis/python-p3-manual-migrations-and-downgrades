"""Renaming students to scholars

Revision ID: 3553e7439646
Revises: 791279dd0760
Create Date: 2023-05-30 21:06:56.316391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3553e7439646'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    


def downgrade() -> None:
    op.rename_table('scholars','students')
    
