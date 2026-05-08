from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    stock_symbol = Column(String(20), nullable=False, index=True)
    stock_price = Column(Float, nullable=False)
    risk_price = Column(Float, nullable=False)
    reward_price = Column(Float, nullable=False)
    risk_amount = Column(Float, nullable=False)
    reward_amount = Column(Float, nullable=False)
    risk_percent = Column(Float, nullable=False)
    reward_percent = Column(Float, nullable=False)
    rr_ratio = Column(Float, nullable=False)
    buy_decision = Column(String(50), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="analyses")
