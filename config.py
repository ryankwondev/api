from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # POSTGRES_URL: str
    SECRET_KEY: str


settings = Settings()

if __name__ == "__main__":
    print(settings.model_dump())
