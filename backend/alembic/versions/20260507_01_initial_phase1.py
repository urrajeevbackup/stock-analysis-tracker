
from datetime import date


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

    op.bulk_insert(
        sa.table(
            "users",
            sa.column("id", sa.Integer()),
            sa.column("full_name", sa.String()),
            sa.column("email", sa.String()),
            sa.column("password_hash", sa.String()),
            sa.column("is_active", sa.Boolean()),
        ),
        [
            {"id": 1, "full_name": "Demo User", "email": "demo@stocktracker.local", "password_hash": "seed_hash_demo", "is_active": True},
            {"id": 2, "full_name": "Trader One", "email": "trader1@stocktracker.local", "password_hash": "seed_hash_trader", "is_active": True},
        ],
    )

    op.bulk_insert(
        sa.table(
            "analyses",
            sa.column("user_id", sa.Integer()),
            sa.column("stock_symbol", sa.String()),
            sa.column("stock_price", sa.Float()),
            sa.column("risk_price", sa.Float()),
            sa.column("reward_price", sa.Float()),
            sa.column("risk_amount", sa.Float()),
            sa.column("reward_amount", sa.Float()),
            sa.column("risk_percent", sa.Float()),
            sa.column("reward_percent", sa.Float()),
            sa.column("rr_ratio", sa.Float()),
            sa.column("buy_decision", sa.String()),
            sa.column("notes", sa.Text()),
        ),
        [
            {
                "user_id": 1,
                "stock_symbol": "TCS",
                "stock_price": 3800.0,
                "risk_price": 3720.0,
                "reward_price": 3960.0,
                "risk_amount": 80.0,
                "reward_amount": 160.0,
                "risk_percent": 2.1053,
                "reward_percent": 4.2105,
                "rr_ratio": 2.0,
                "buy_decision": "Buy",
                "notes": "Seed analysis record",
            }
        ],
    )


    op.bulk_insert(
        sa.table(
            "trades",
            sa.column("id", sa.Integer()),
            sa.column("user_id", sa.Integer()),
            sa.column("stock_symbol", sa.String()),
            sa.column("trade_type", sa.String()),
            sa.column("entry_price", sa.Float()),
            sa.column("entry_date", sa.Date()),
            sa.column("stop_loss", sa.Float()),
            sa.column("target_price", sa.Float()),
            sa.column("status", sa.String()),
            sa.column("notes", sa.Text()),
        ),
        [
            {
                "id": 1,
                "user_id": 1,
                "stock_symbol": "INFY",
                "trade_type": "Swing",
                "entry_price": 1450.0,
                "entry_date": date(2026, 5, 1),
                "stop_loss": 1400.0,
                "target_price": 1550.0,
                "status": "OPEN",
                "notes": "Seed trade record",
            }
        ],
    )

    op.bulk_insert(
        sa.table(
            "trade_trails",
            sa.column("trade_id", sa.Integer()),
            sa.column("old_stop_loss", sa.Float()),
            sa.column("new_stop_loss", sa.Float()),
            sa.column("old_target_price", sa.Float()),
            sa.column("new_target_price", sa.Float()),
            sa.column("notes", sa.Text()),
        ),
        [
            {
                "trade_id": 1,
                "old_stop_loss": 1400.0,
                "new_stop_loss": 1420.0,
                "old_target_price": 1550.0,
                "new_target_price": 1580.0,
                "notes": "Initial trail adjustment",
            }
        ],
    )




def downgrade() -> None:
    op.drop_table("uploads")
    op.drop_table("trade_trails")
    op.drop_table("trades")
    op.drop_table("analyses")
    op.drop_table("users")
