from datetime import datetime
from pydantic import BaseModel


class TradeTrailCreate(BaseModel):
    trade_id: int
    new_stop_loss: float | None = None
    new_target_price: float | None = None
    notes: str | None = None


class TradeTrailResponse(BaseModel):
    id: int
    trade_id: int
    old_stop_loss: float | None = None
    new_stop_loss: float | None = None
    old_target_price: float | None = None
    new_target_price: float | None = None
    notes: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True
