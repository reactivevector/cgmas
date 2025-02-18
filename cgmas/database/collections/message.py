import logging
from datetime import datetime

from bson import ObjectId

from cgmas.database import get_collection
from cgmas.database.model import DbBaseModel

LOGGER = logging.getLogger(__name__)


class Message(DbBaseModel):
	text: str
	created_at: datetime = datetime.now()


def find_messages() -> list[Message]:
	try:
		collection = get_collection('messages')
		messages = Message.from_mongos(collection.find_all({}))
	except Exception as e:
		LOGGER.error(f'Error finding messages: {e}')
		raise e

	return messages


def insert_message(message: dict) -> Message:
	try:
		collection = get_collection('messages')
		result = collection.insert_one(message)
		updated_message = Message.from_mongo(
			collection.find_one({'_id': ObjectId(result.inserted_id)})
		)
	except Exception as e:
		LOGGER.error(f'Error insert message: {e}')
		raise e

	return updated_message


def update_message(filters: dict, message: dict) -> Message:
	try:
		collection = get_collection('messages')
		updates = {'$set': message}
		result = collection.update_one(filters, updates)
		updated_message = Message.from_mongo(
			collection.find_one({'_id': ObjectId(result.upserted_id)})
		)
	except Exception as e:
		LOGGER.error(f'Error update message: {e}')
		raise e

	return updated_message


def delete_message(message_id: str) -> int:
	try:
		collection = get_collection('messages')
		filters = {'_id': ObjectId(message_id)}
		result = collection.delete_one(filters)
	except Exception as e:
		LOGGER.error(f'Error delete message: {e}')
		raise e

	return result.deleted_count
