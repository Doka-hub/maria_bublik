import aioredis

import json

from utils.redis import Redis


async def get_user_info(client: aioredis.Redis, user_id: int) -> dict:
    user_info = json.loads(await client.hget('users', user_id) or '{}')
    return user_info


async def get_spam_warnings(user_id: int) -> int:
    redis = Redis()
    client = await redis.client

    user_info = await get_user_info(client, user_id)
    spam_warnings = user_info.get('spam_warnings', 0)
    await redis.disconnect()
    return spam_warnings


async def set_spam_warnings(user_id: int, count: int):
    redis = Redis()
    client = await redis.client

    user_info = await get_user_info(client, user_id)
    spam_warnings = user_info.get('spam_warnings', 0)
    user_info.update({'spam_warnings': spam_warnings + count})
    await client.hset('users', user_id, json.dumps(user_info))
    await redis.disconnect()


async def clear_spam_warnings(user_id: int):
    redis = Redis()
    client = await redis.client

    user_info = await get_user_info(client, user_id)
    user_info.update({'spam_warnings': 0})
    await client.hset('users', user_id, json.dumps(user_info))
    await redis.disconnect()
