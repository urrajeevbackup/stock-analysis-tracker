from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.trade import Trade
from app.models.trade_trail import TradeTrail
from app.schemas.trade_trail import TradeTrailCreate, TradeTrailResponse

router = APIRouter(tags=["trade_trails"])


@router.post("/", response_model=TradeTrailResponse)
def create_trail(payload: TradeTrailCreate, db: Session = Depends(get_db)):
    trade = db.query(Trade).filter(Trade.id == payload.trade_id).first()
    if not trade:
        raise HTTPException(status_code=404, detail="Trade not found")
    trail = TradeTrail(
        trade_id=trade.id,
        old_stop_loss=trade.stop_loss,
        new_stop_loss=payload.new_stop_loss,
        old_target_price=trade.target_price,
        new_target_price=payload.new_target_price,
        notes=payload.notes,
    )
    if payload.new_stop_loss is not None:
        trade.stop_loss = payload.new_stop_loss
    if payload.new_target_price is not None:
        trade.target_price = payload.new_target_price
    db.add(trail)
    db.commit()
    db.refresh(trail)
    return trail


@router.get("/{trade_id}", response_model=list[TradeTrailResponse])
def list_trails(trade_id: int, db: Session = Depends(get_db)):
    return db.query(TradeTrail).filter(TradeTrail.trade_id == trade_id).order_by(TradeTrail.created_at.desc()).all()
