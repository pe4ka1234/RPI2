from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    VERSION: str = '0.1.0'

    # Кому интересно про CORS, почитайте тут: https://fastapi.tiangolo.com/tutorial/cors/
    CORS_ORIGINS: List[str] = ['*']
    PORT: int = 5000
    URL_PREFIX: str = '/api/v1'

    # НЕЛЬЗЯ ЗАПУШИТЬ ЭТОТ ИЛИ ДРУГИЕ ТОКЕНЫ НА ГИТХАБ. ДОБАВЬТЕ config.py в gitignore!
    GITHUB_API_TOKEN: str = "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"


settings = Settings()
