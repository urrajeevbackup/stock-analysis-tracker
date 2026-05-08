from fastapi import HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

engine = create_engine(settings.resolved_database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        # Force a lightweight connection checkout early so auth/dependency issues
        # are reported as a clear API error instead of an unhandled 500 trace.
        db.connection()
        yield db
    except RuntimeError as exc:
        if "cryptography" in str(exc):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=(
                    "Database authentication requires the 'cryptography' package. "
                    "Install it with: pip install cryptography"
                ),
            ) from exc
        raise
    except SQLAlchemyError as exc:
        safe_db_url = make_url(settings.resolved_database_url).render_as_string(
            hide_password=True
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                f"Database connection failed: {exc.__class__.__name__}: {exc}. "
                f"Target={safe_db_url}"
            ),
        ) from exc
    finally:
        db.close()
