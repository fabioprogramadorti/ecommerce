# Order Integration System

Sistema de integração de pedidos baseado em pipeline de dados (ETL), com processamento assíncrono via fila, envio para API externa, persistência em banco de dados e testes automatizados.

---

## Visão geral

O sistema realiza:

- Leitura de pedidos via CSV
- Transformação e padronização de dados (ETL)
- Enfileiramento dos pedidos no RabbitMQ
- Processamento assíncrono via worker
- Envio para API externa
- Persistência em PostgreSQL
- Geração de relatório agregado
- Execução de testes automatizados via Docker

---

## Arquitetura

CSV → ETL → RabbitMQ → Worker → API → PostgreSQL

---

## Tecnologias

- Python 3.11
- FastAPI
- PostgreSQL
- RabbitMQ
- Docker & Docker Compose
- SQLAlchemy
- Requests
- Pytest

---

## Estrutura do projeto

```
app/
├── application/
│   └── use_cases/
├── domain/
│   └── dtos/
├── infrastructure/
│   ├── api/
│   ├── csv/
│   ├── database/
│   └── queue/
├── interfaces/
│   └── api.py
├── ArquivoParaTeste/
│   └── orders.csv

tests/

docker-compose.yml
Dockerfile
```

---

## Pré-requisitos

O único requisito para execução do projeto é:

- Docker
- Docker Compose

---

## Observação importante

Toda a infraestrutura da aplicação é executada via Docker.

Não é necessário instalar:

- Python localmente
- PostgreSQL localmente
- RabbitMQ localmente
- Dependências manualmente
- Ambiente virtual (venv)

O projeto foi desenhado para garantir:

- Ambiente 100% replicável
- Isolamento entre serviços
- Facilidade de execução
- Simulação de ambiente real de produção

---

## Como executar o projeto

### 1. Subir todos os serviços

```
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

### 2. Executar testes automatizados

```
docker-compose up tests
```

### 3. Acessar API

http://localhost:8000/docs

---

## RabbitMQ

### Acessar painel web

http://localhost:15672

### Credenciais padrão

User: guest
Password: guest

### O que verificar

- Fila chamada "orders"
- Mensagens sendo enfileiradas
- Consumo pelo worker

---

## Banco de dados (PostgreSQL)

O banco roda dentro do container Docker.

Não é necessário instalar PostgreSQL localmente.

### Acessar via container

```
docker exec -it orders_db psql -U postgres -d orders
```

### Consultar dados

```
SELECT * FROM orders;
```

### Dados de conexão

Host: localhost
Port: 5432
Database: orders
User: postgres
Password: postgres

---

## Importação de pedidos

### Endpoint

POST /orders/import

### Arquivo de teste incluído

ArquivoParaTeste/orders.csv

---

## Teste via Postman

O projeto inclui uma collection do Postman pronta para uso.

### Importar collection

1. Abrir o Postman
2. Clicar em Import
3. Selecionar a collection do projeto

### Requisição POST

POST http://localhost:8000/orders/import

### Configuração obrigatória

Body → form-data

Key | Type | Value
----|------|------
file | File | ArquivoParaTeste/orders.csv

O nome do campo deve ser exatamente:

file

Caso contrário, a API retornará erro de campo obrigatório.

### Requisição GET

GET http://localhost:8000/orders/report

---

## Fluxo do sistema

1. Upload do CSV via API
2. ETL (validação e transformação)
3. Envio para fila (RabbitMQ)
4. Worker consome os pedidos
5. Integração com API externa
6. Persistência no PostgreSQL
7. Geração de relatório

---

## Relatório

### Endpoint

GET /orders/report

### Retorna:

- Total por status
- Valor total por status
- Arquivo CSV gerado

---

## Testes automatizados

```
docker-compose up tests
```

---

## Serviços

- db → PostgreSQL
- rabbitmq → fila de mensagens
- app → API FastAPI
- worker → consumidor da fila
- tests → execução de testes

---

## Diferenciais

- Pipeline ETL estruturado
- Processamento assíncrono com RabbitMQ
- Arquitetura em camadas
- Integração com API externa
- Persistência em banco relacional
- Testes automatizados
- Ambiente totalmente containerizado

---

## Autor

Nome: Fabio Moura dos Santos
Email: ashiratecnologia@gmail.com
