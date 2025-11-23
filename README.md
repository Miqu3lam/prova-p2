🛠️ Instalação🚖 TransFlow – Sistema de Processamento de Corridas

Este projeto implementa uma arquitetura baseada em mensageria usando FastAPI, RabbitMQ, MongoDB, Redis e FastStream, simulando o processamento de corridas e atualização de saldo de motoristas.

O sistema conta com:

API FastAPI para envio de eventos

Producer enviando mensagens para RabbitMQ

Consumer processando eventos

MongoDB para armazenar corridas

Redis para armazenar saldo dos motoristas

Toda a stack rodando via Docker


📦 1. Instalação
🔧 Pré-requisitos

Certifique-se de que você tem instalado:

Docker

Docker Compose

Python 3.10+ (apenas se quiser rodar localmente sem Docker)

Git


📥 Clonando o repositório
git clone https://github.com/Miqu3lam/prova-p2

cd transflow_fixed

▶️ Subindo a aplicação

Para iniciar todos os serviços:

docker compose up --build

Os containers iniciados serão:

FastAPI (transflow_app)

Consumer (transflow_consumer)

RabbitMQ + Dashboard

MongoDB

Redis



🔐 2. Variáveis de ambiente necessárias

As variáveis já estão definidas no docker-compose.yml, mas podem ser sobrescritas em .env se você quiser.

🔧 FastAPI
Variável	Descrição
MONGO_URL	URL do MongoDB
REDIS_URL	URL do Redis
🔧 Consumer
Variável	Descrição
RABBITMQ_URL	URL do RabbitMQ
MONGO_URL	URL do MongoDB
REDIS_URL	URL do Redis

Valores padrão (já configurados):

RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
MONGO_URL=mongodb://mongo:27017
REDIS_URL=redis://redis:6379



🚀 3. Uso da API

Depois que os containers estiverem rodando, abra no navegador:

👉 Swagger UI:
http://localhost:8000/docs

📌 Enviar corrida (POST /corridas)

Exemplo de corpo da requisição:

{
  "id_corrida": "123",
  "passageiro": {
    "nome": "João"
  },
  "motorista": {
    "nome": "Carlos"
  },
  "origem": "Rua A",
  "destino": "Rua B",
  "valor_corrida": 25.50,
  "forma_pagamento": "pix"
}

📌 Listar corridas (GET /corridas)

Retorna todas as corridas salvas no MongoDB.

📌 Filtrar corridas (GET /corridas/{forma_pagamento})

Exemplo:

/corridas/dinheiro

📌 Consultar saldo do motorista (GET /saldo/{motorista})

Exemplo:

/saldo/João



🧪 4. Como testar o fluxo completo

Vá em POST /corridas no Swagger

Envie uma corrida

O Producer envia o evento para o RabbitMQ

O Consumer recebe, processa e:
✔ Salva a corrida no MongoDB
✔ Atualiza o saldo no Redis

Vá em GET /corridas → corrida aparece

Vá em GET /saldo/{motorista} → saldo atualizado aparece

🖼 5. Captura de tela

![alt text](<imagens/Captura de tela 2025-11-23 005621.png>)

![alt text](<imagens/Captura de tela 2025-11-23 010502.png>)
