
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client.transflow

async def salvar_corrida(data):
    await db.corridas.insert_one(data)

async def listar_corridas():
    return await db.corridas.find().to_list(None)

async def filtrar_corridas(forma):
    return await db.corridas.find({"forma_pagamento": forma}).to_list(None)
