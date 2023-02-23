import json
from datetime import datetime
from typing import Any
from bson import ObjectId


class MongoJSONEncoder(json.JSONEncoder):
    """Personal Mongo Json-Encoder, to return ObjIDs of MongoDB."""
    def default(self, o: Any) -> Any:
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

