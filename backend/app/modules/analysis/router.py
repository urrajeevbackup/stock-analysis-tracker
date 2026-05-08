from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.analysis import Analysis
from app.schemas.analysis import AnalysisCreate, AnalysisResponse, AnalysisUpdate

router = APIRouter(tags=["analysis"])


def calculate_analysis_fields(stock_price: float, risk_price: float, reward_price: float):
    risk_amount = stock_price - risk_price
    reward_amount = reward_price - stock_price
    risk_percent = (risk_amount / stock_price) * 100 if stock_price else 0
    reward_percent = (reward_amount / stock_price) * 100 if stock_price else 0
    rr_ratio = (reward_amount / risk_amount) if risk_amount else 0
    return risk_amount, reward_amount, risk_percent, reward_percent, rr_ratio


@router.post("/", response_model=AnalysisResponse)
def create_analysis(payload: AnalysisCreate, db: Session = Depends(get_db)):
    risk_amount, reward_amount, risk_percent, reward_percent, rr_ratio = calculate_analysis_fields(
        payload.stock_price, payload.risk_price, payload.reward_price
    )
    analysis = Analysis(**payload.model_dump(), risk_amount=risk_amount, reward_amount=reward_amount, risk_percent=risk_percent, reward_percent=reward_percent, rr_ratio=rr_ratio)
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    return analysis


@router.get("/", response_model=list[AnalysisResponse])
def list_analysis(db: Session = Depends(get_db)):
    return db.query(Analysis).order_by(Analysis.created_at.desc()).all()


@router.get("/{item_id}", response_model=AnalysisResponse)
def get_analysis(item_id: int, db: Session = Depends(get_db)):
    analysis = db.query(Analysis).filter(Analysis.id == item_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return analysis


@router.put("/{item_id}", response_model=AnalysisResponse)
def update_analysis(item_id: int, payload: AnalysisUpdate, db: Session = Depends(get_db)):
    analysis = db.query(Analysis).filter(Analysis.id == item_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(analysis, key, value)
    risk_amount, reward_amount, risk_percent, reward_percent, rr_ratio = calculate_analysis_fields(
        analysis.stock_price, analysis.risk_price, analysis.reward_price
    )
    analysis.risk_amount = risk_amount
    analysis.reward_amount = reward_amount
    analysis.risk_percent = risk_percent
    analysis.reward_percent = reward_percent
    analysis.rr_ratio = rr_ratio
    db.commit()
    db.refresh(analysis)
    return analysis
