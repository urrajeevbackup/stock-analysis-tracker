from fastapi import FastAPI

from app.core.config import settings
from app.modules.alerts.router import router as alerts_router
from app.modules.analysis.router import router as analysis_router
from app.modules.reports.router import router as reports_router
from app.modules.trade_trails.router import router as trade_trails_router
from app.modules.trades.router import router as trades_router
from app.modules.uploads.router import router as uploads_router

app = FastAPI(title=settings.app_name)


@app.get(f"{settings.api_v1_prefix}/health", tags=["health"])
def health_check():
    return {"status": "ok"}


app.include_router(analysis_router, prefix=f"{settings.api_v1_prefix}/analysis")
app.include_router(trades_router, prefix=f"{settings.api_v1_prefix}/trades")
app.include_router(trade_trails_router, prefix=f"{settings.api_v1_prefix}/trade-trails")
app.include_router(alerts_router, prefix=f"{settings.api_v1_prefix}/alerts")
app.include_router(reports_router, prefix=f"{settings.api_v1_prefix}/reports")
app.include_router(uploads_router, prefix=f"{settings.api_v1_prefix}/uploads")
