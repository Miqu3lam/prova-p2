import json
import os
import time
from faststream import FastStream
from faststream.rabbit import RabbitBroker

from src.database.mongo_client import salvar_corrida
from src.database.redis_client import aumentar_saldo

RABBIT_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")

broker = RabbitBroker(RABBIT_URL)

# --- Retry para esperar RabbitMQ levantar ---
MAX_RETRIES = 15
DELAY = 2

for attempt in range(MAX_RETRIES):
    try:
        print(f"🔄 Tentando conectar ao RabbitMQ ({attempt+1}/{MAX_RETRIES})...")
        broker._connection
        print("✅ Conectado ao RabbitMQ!")
        break
    except Exception as e:
        print("❌ RabbitMQ ainda não está pronto:", e)
        time.sleep(DELAY)
else:
    raise RuntimeError("RabbitMQ não iniciou após várias tentativas")

# -------------------------------------------------

app = FastStream(broker)

@broker.subscriber("corridas.finalizadas")
async def processar_corrida(msg: str):
    dados = json.loads(msg)
    motorista = dados["motorista"]["nome"]
    valor = float(dados["valor_corrida"])

    await aumentar_saldo(motorista, valor)
    await salvar_corrida(dados)
