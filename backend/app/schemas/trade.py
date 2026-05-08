from datetime import date, datetime
from pydantic import BaseModel


class TradeBase(BaseModel):
    user_id: int
    stock_symbol: str
    trade_type: str
    entry_price: float
    entry_date: date
    exit_price: float | None = None
    exit_date: date | None = None
    stop_loss: float
    target_price: float
    status: str
    notes: str | None = None


class TradeCreate(TradeBase):
    pass


class TradeUpdate(BaseModel):
    stock_symbol: str | None = None
    trade_type: str | None = None
    entry_price: float | None = None
    entry_date: date | None = None
    exit_price: float | None = None
    exit_date: date | None = None
    stop_loss: float | None = None
    target_price: float | None = None
    status: str | None = None
    notes: str | None = None


class TradeResponse(TradeBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
