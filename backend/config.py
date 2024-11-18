from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    VERSION: str = '0.1.0'

    CORS_ORIGINS: List[str] = ['*']
    PORT: int = 5000
    URL_PREFIX: str = '/api/v1'

    # далее нужно подставить свой токен
    GITHUB_API_TOKEN: str = "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"


settings = Settings()
