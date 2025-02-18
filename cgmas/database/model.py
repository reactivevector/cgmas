from pydantic import BaseModel


class DbBaseModel(BaseModel):
	id: str

	@classmethod
	def from_mongo(cls, data: dict):
		if '_id' in data:
			data['id'] = str(data['_id'])
			del data['_id']
		return cls(**data)

	@classmethod
	def from_mongos(cls, documents: dict):
		return [cls.from_mongo(doc) for doc in documents]
