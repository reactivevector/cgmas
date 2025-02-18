from .exception import DbException
from .mongodb import MongoDbClient, MongoDbCollection, MongoDbConfig, create_mongo_db

_DATABASE: MongoDbClient = None


def setup_database(options: MongoDbConfig):
	global _DATABASE
	_DATABASE = create_mongo_db(options)


def get_database_client() -> MongoDbClient:
	if not _DATABASE:
		raise DbException('Database not initialized')
	return _DATABASE


def get_collection(name: str) -> MongoDbCollection:
	return get_database_client().get_collection(name)
