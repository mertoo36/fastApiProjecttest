from pydantic import BaseModel

"""
All classes for post-requests are stored in here
"""


class Country(BaseModel):
    name: str
    description: str
