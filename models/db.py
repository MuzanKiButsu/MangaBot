from motor.motor_asyncio import AsyncIOMotorClient
from bot import Vars
import time

# Connect to Mongo
client = AsyncIOMotorClient(Vars.DB_URL)
db = client[Vars.DB_NAME]

subs = db["subs"]
users = db["users"]
acollection = db["premium"]

# Initialize default docs if missing
async def init_db():
    if not await subs.find_one({"_id": "data"}):
        await subs.insert_one({"_id": "data"})

    if not await users.find_one({"_id": Vars.DB_NAME}):
        await users.insert_one({"_id": Vars.DB_NAME})

# ---- Premium ----
async def add_premium(user_id, time_limit_days):
    expiration_timestamp = int(time.time()) + time_limit_days * 86400
    await acollection.update_one(
        {"user_id": user_id},
        {"$set": {"expiration_timestamp": expiration_timestamp}},
        upsert=True
    )

async def remove_premium(user_id):
    await acollection.delete_one({"user_id": user_id})

async def remove_expired_users():
    current_timestamp = int(time.time())
    await acollection.delete_many({"expiration_timestamp": {"$lte": current_timestamp}})

async def premium_user(user_id):
    user = await acollection.find_one({"user_id": user_id})
    return user is not None

# ---- Subscriptions ----
async def get_users():
    cursor = users.find({}, {"_id": 1})
    return [doc["_id"] async for doc in cursor]

async def add_sub(user_id, manga_url: str):
    user_id = str(user_id)

    # Add user to subs
    await subs.update_one(
        {"_id": "data"},
        {"$addToSet": {f"{manga_url}.users": user_id}},
        upsert=True
    )

    # Add manga to user
    await users.update_one(
        {"_id": Vars.DB_NAME},
        {"$addToSet": {f"{user_id}.subs": manga_url}},
        upsert=True
    )

async def get_subs(user_id, manga_url: str = None):
    user_id = str(user_id)
    doc = await users.find_one({"_id": Vars.DB_NAME}, {f"{user_id}": 1})
    if not doc or user_id not in doc:
        return []

    subs_list = doc[user_id].get("subs", [])

    if manga_url:
        return manga_url in subs_list
    return subs_list

async def delete_sub(user_id, manga_url: str):
    user_id = str(user_id)

    await subs.update_one(
        {"_id": "data"},
        {"$pull": {f"{manga_url}.users": user_id}}
    )

    await users.update_one(
        {"_id": Vars.DB_NAME},
        {"$pull": {f"{user_id}.subs": manga_url}}
    )
