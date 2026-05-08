from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.trade import Trade
from app.schemas.trade import TradeCreate, TradeResponse, TradeUpdate

router = APIRouter(tags=["trades"])


@router.post("/", response_model=TradeResponse)
def create_trade(payload: TradeCreate, db: Session = Depends(get_db)):
    trade = Trade(**payload.model_dump())
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade


@router.get("/", response_model=list[TradeResponse])
def list_trades(db: Session = Depends(get_db)):
    return db.query(Trade).order_by(Trade.created_at.desc()).all()


@router.get("/{item_id}", response_model=TradeResponse)
def get_trade(item_id: int, db: Session = Depends(get_db)):
    trade = db.query(Trade).filter(Trade.id == item_id).first()
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    return trade


@router.put("/{item_id}", response_model=TradeResponse)
def update_trade(item_id: int, payload: TradeUpdate, db: Session = Depends(get_db)):
    trade = db.query(Trade).filter(Trade.id == item_id).first()
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(trade, key, value)
    db.commit()
    db.refresh(trade)
    return trade
