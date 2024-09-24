from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    REDIS_PASSWORD: str
    REDIS_USER: str
    REDIS_USER_PASSWORD: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str
    S3_ENDPOINT_URL: str
    S3_BUCKET_NAME: str

    BACKEND_CORS_ORIGINS: str

    @property
    def POSTGRES_DATABASE_URI(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    @property
    def REDIS_URI(self):
        return f"redis://0.0.0.0:6380"


    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()