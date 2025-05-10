import os
import pathlib
from functools import lru_cache

from dotenv import load_dotenv
load_dotenv()

class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASE_CONNECT_DICT: dict = {}
    DB_NAME: str = os.environ.get('DB_NAME')
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('DB_PORT', 3306)
    DB_USER: str = os.environ.get('DB_USER')
    DB_PASS: str = os.environ.get('DB_PASS')

class DevelopmentConfig(BaseConfig):
    DATABASE_URL: str = f'mysql+pymysql://{BaseConfig.DB_USER}:{BaseConfig.DB_PASS}@{BaseConfig.DB_HOST}:{BaseConfig.DB_PORT}/{BaseConfig.DB_NAME}'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

@lru_cache()
def get_settings() -> DevelopmentConfig | ProductionConfig | TestingConfig:
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()

settings = get_settings()