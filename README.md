# Order Integration System

Sistema de integração de pedidos baseado em pipeline de dados (ETL), com envio para API externa, persistência em banco de dados e testes automatizados.

---

# Visão geral

O sistema realiza:

- Leitura de pedidos via CSV
- Transformação e padronização de dados (ETL)
- Envio para API externa
- Persistência em PostgreSQL
- Geração de relatório agregado
- Execução de testes automatizados via Docker

---

# Arquitetura

CSV → ETL → API → PostgreSQL

---

# Tecnologias

- Python 3.11
- FastAPI
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy
- Requests
- Pytest

---

# Estrutura do projeto
```text
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

---

# Pré-requisitos

- Docker
- Docker Compose

---

# Como executar o projeto

## 1. Subir todos os serviços

docker-compose down -v  
docker-compose build --no-cache  
docker-compose up  

---

## 1.1 Executar testes automatizados

docker-compose up tests  

---

## 2. Acessar API

http://localhost:8000/docs  

---

## 3. Banco de dados

Host: localhost  
Port: 5432  
Database: orders  
User: postgres  
Password: postgres  

---

# Importação de pedidos

## Endpoint

POST /orders/import  

## Arquivo de teste incluído

Este projeto já contém uma pasta chamada:

ArquivoParaTeste/

Ela contém um arquivo CSV pronto para execução do sistema:

```text
ArquivoParaTeste/orders.csv
