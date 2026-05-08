from datetime import datetime
from pydantic import BaseModel


class AnalysisBase(BaseModel):
    user_id: int
    stock_symbol: str
    stock_price: float
    risk_price: float
    reward_price: float
    buy_decision: str
    notes: str | None = None


class AnalysisCreate(AnalysisBase):
    pass


class AnalysisUpdate(BaseModel):
    stock_symbol: str | None = None
    stock_price: float | None = None
    risk_price: float | None = None
    reward_price: float | None = None
    buy_decision: str | None = None
    notes: str | None = None


class AnalysisResponse(BaseModel):
    id: int
    user_id: int
    stock_symbol: str
    stock_price: float
    risk_price: float
    reward_price: float
    risk_amount: float
    reward_amount: float
    risk_percent: float
    reward_percent: float
    rr_ratio: float
    buy_decision: str
    notes: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True
