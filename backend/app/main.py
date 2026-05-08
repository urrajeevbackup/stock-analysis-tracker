from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.models import analysis, trade, trade_trail, user  # noqa: F401
from app.modules.analysis.router import router as analysis_router
from app.modules.trade_trails.router import router as trade_trails_router
from app.modules.trades.router import router as trades_router


def register_routers(app: FastAPI) -> None:
    app.include_router(analysis_router, prefix=f"{settings.api_v1_prefix}/analysis")
    app.include_router(trades_router, prefix=f"{settings.api_v1_prefix}/trades")
    app.include_router(trade_trails_router, prefix=f"{settings.api_v1_prefix}/trade-trails")


app = FastAPI(title=settings.app_name)


@app.on_event("startup")
def ensure_tables_exist() -> None:
    """Create tables if migrations have not been applied yet."""
    Base.metadata.create_all(bind=engine)


@app.get(f"{settings.api_v1_prefix}/health", tags=["health"])
def health_check():
    return {"status": "ok"}


register_routers(app)
