from fastapi import FastAPI
from pydantic import BaseModel

from src.producer import broker, publish_corrida_finalizada
from src.database.mongo_client import listar_corridas, salvar_corrida, filtrar_corridas
from src.database.redis_client import get_saldo


class Corrida(BaseModel):
    id_corrida: str
    passageiro: dict
    motorista: dict
    origem: str
    destino: str
    valor_corrida: float
    forma_pagamento: str


app = FastAPI()


# ===============================
# INICIAR E PARAR O BROKER
# ===============================
@app.on_event("startup")
async def start_broker():
    await broker.start()
    print("🐇 RabbitMQ Producer conectado!")


@app.on_event("shutdown")
async def stop_broker():
    await broker.close()
    print("🐇 RabbitMQ Producer desconectado!")


# ===============================
# ROTAS
# ===============================
@app.post("/corridas")
async def criar_corrida(corrida: Corrida):
    """
    Envia o evento de corrida finalizada para o RabbitMQ
    """
    await publish_corrida_finalizada(corrida.dict())
    return {"status": "Evento enviado com sucesso!"}


@app.get("/corridas")
async def listar():
    """
    Retorna todas as corridas armazenadas no MongoDB
    """
    return await listar_corridas()


@app.get("/corridas/{forma}")
async def por_forma(forma: str):
    """
    Filtra corridas pela forma de pagamento
    """
    return await filtrar_corridas(forma)


@app.get("/saldo/{motorista}")
async def saldo(motorista: str):
    """
    Consulta o saldo do motorista no Redis
    """
    return await get_saldo(motorista)
