from starlette.config import Config

config = Config(".env")

# DATABASE_URL = config("FASTAPI_DATABASE_URL", cast=str, default="")
DATABASE_URL = "postgresql+asyncpg://parser:parser@localhost:5432/fastapi_study_db"
