from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from classes import *
from dbconn import get_db
from utils import *
import json

app = FastAPI()

api_keys = ["O=Gn#0XmH:5:F.PaYr-3+mDVEcH'WY"]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def api_key_auth(api_key: str = Depends(oauth2_scheme)):
    """Securing WS with API-Key authentication"""
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Forbidden"
        )


@app.get("/", dependencies=[Depends(api_key_auth)])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", dependencies=[Depends(api_key_auth)])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Returns payload as JSON
@app.get("/test/path/{query}", dependencies=[Depends(api_key_auth)])
async def test_query(query: str):
    value = "value"

    x = {
        "message": query,
        "Test": value
    }

    # json.loads(json.dumps(<var>)) converts string to JSON without backslashes

    return json.loads(json.dumps(x))


@app.get("/db", dependencies=[Depends(api_key_auth)])
async def get_all_db_entry():
    """Returns all entries from DB."""
    db = await get_db()
    coll = db["wwi21amb"]
    output = coll.find()
    return json.loads(MongoJSONEncoder().encode(list(output)))


@app.post("/test/post", dependencies=[Depends(api_key_auth)])
async def post_example(country: Country):
    """Test function for POSTing data. Data will not be saved in DB!"""
    print(country.name)
    return {"message": f"Your country is: {country.name}"}


@app.post("/test/post/country", dependencies=[Depends(api_key_auth)])
async def post_db(country: Country):
    """POST country name to database."""
    db = await get_db()
    coll = db["wwi21amb"]
    # Post only name, because column "wwwi21amb" got only name as "row"
    obj = {"name": country.name}
    x = coll.insert_one(obj)
    return {"message": f"Success: {x}"}

#test for git commit