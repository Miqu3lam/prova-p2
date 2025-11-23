
from faststream.rabbit import RabbitBroker
import json
import os

RABBIT_URL = os.getenv("RABBIT_URL", "amqp://guest:guest@rabbitmq:5672/")
broker = RabbitBroker(RABBIT_URL)

async def publish_corrida_finalizada(corrida: dict):
    await broker.publish(
        message=json.dumps(corrida),
        routing_key="corridas.finalizadas",
    )
