from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    stock_symbol = Column(String(20), nullable=False, index=True)
    trade_type = Column(String(20), nullable=False)
    entry_price = Column(Float, nullable=False)
    entry_date = Column(Date, nullable=False)
    exit_price = Column(Float, nullable=True)
    exit_date = Column(Date, nullable=True)
    stop_loss = Column(Float, nullable=False)
    target_price = Column(Float, nullable=False)
    status = Column(String(30), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="trades")
    trails = relationship("TradeTrail", back_populates="trade", cascade="all, delete-orphan")
