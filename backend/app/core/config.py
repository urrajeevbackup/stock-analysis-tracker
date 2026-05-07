from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Stock Analysis Tracker API"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "mysql+pymysql://root:password@localhost:3306/stock_tracker"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
