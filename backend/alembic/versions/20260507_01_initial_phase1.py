"""initial phase1 schema

Revision ID: 20260507_01
Revises:
Create Date: 2026-05-07
"""
from alembic import op
import sqlalchemy as sa


revision = "20260507_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_users_id", "users", ["id"])
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "analyses",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("stock_symbol", sa.String(length=20), nullable=False),
        sa.Column("stock_price", sa.Float(), nullable=False),
        sa.Column("risk_price", sa.Float(), nullable=False),
        sa.Column("reward_price", sa.Float(), nullable=False),
        sa.Column("risk_amount", sa.Float(), nullable=False),
        sa.Column("reward_amount", sa.Float(), nullable=False),
        sa.Column("risk_percent", sa.Float(), nullable=False),
        sa.Column("reward_percent", sa.Float(), nullable=False),
        sa.Column("rr_ratio", sa.Float(), nullable=False),
        sa.Column("buy_decision", sa.String(length=50), nullable=False),
        sa.Column("notes", sa.Text()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_analyses_id", "analyses", ["id"])

    op.create_table(
        "trades",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("stock_symbol", sa.String(length=20), nullable=False),
        sa.Column("trade_type", sa.String(length=20), nullable=False),
        sa.Column("entry_price", sa.Float(), nullable=False),
        sa.Column("entry_date", sa.Date(), nullable=False),
        sa.Column("exit_price", sa.Float()),
        sa.Column("exit_date", sa.Date()),
        sa.Column("stop_loss", sa.Float(), nullable=False),
        sa.Column("target_price", sa.Float(), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("notes", sa.Text()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "trade_trails",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("trade_id", sa.Integer(), sa.ForeignKey("trades.id"), nullable=False),
        sa.Column("old_stop_loss", sa.Float()),
        sa.Column("new_stop_loss", sa.Float()),
        sa.Column("old_target_price", sa.Float()),
        sa.Column("new_target_price", sa.Float()),
        sa.Column("notes", sa.Text()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "uploads",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("entity_type", sa.String(length=100), nullable=False),
        sa.Column("entity_id", sa.Integer(), nullable=False),
        sa.Column("file_url", sa.String(length=500), nullable=False),
        sa.Column("file_name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("uploads")
    op.drop_table("trade_trails")
    op.drop_table("trades")
    op.drop_table("analyses")
    op.drop_table("users")
