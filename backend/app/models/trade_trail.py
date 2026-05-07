from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Text, func

from app.core.database import Base


class TradeTrail(Base):
    __tablename__ = "trade_trails"

    id = Column(Integer, primary_key=True, index=True)
    trade_id = Column(Integer, ForeignKey("trades.id"), nullable=False, index=True)
    old_stop_loss = Column(Float, nullable=True)
    new_stop_loss = Column(Float, nullable=True)
    old_target_price = Column(Float, nullable=True)
    new_target_price = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
