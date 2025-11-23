
import redis.asyncio as redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
r = redis.from_url(REDIS_URL, decode_responses=True)

async def aumentar_saldo(motorista: str, valor: float):
    await r.incrbyfloat(f"saldo:{motorista}", valor)

async def get_saldo(motorista: str):
    return await r.get(f"saldo:{motorista}")
