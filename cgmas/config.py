from pydantic import BaseModel

from cgmas.cache import CacheConfig, setup_cache
from cgmas.database import setup_database
from cgmas.database.mongodb import MongoDbConfig
from cgmas.logging import setup_logging
from cgmas.logging.config import LoggingConfig


class AppConfig(BaseModel):
	mongodb: MongoDbConfig

	cache: CacheConfig

	logging: LoggingConfig


def setup_app_config(config: AppConfig):
	setup_cache(config.cache)
	setup_database(config.mongodb)
	setup_logging(config.logging)
