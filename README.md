#  Order Integration System

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

# 📁 Estrutura do projeto

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
tests/
docker-compose.yml
Dockerfile

---

# ⚙️ Pré-requisitos

- Docker
- Docker Compose

---

# 🚀 Como executar o projeto

## 1. Subir todos os serviços

docker-compose down -v  
docker-compose build --no-cache
docker-compose up

---

## 1.1 Acessar Teste API

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

## Exemplo de CSV

id_pedido,cliente,valor,status
1,Ana,100,pending
2,Bia,200,approved
3,Carlos,300,canceled

---

# Relatório

## Endpoint

GET /orders/report

Retorna:

- Total por status
- Valor total por status
- CSV gerado

---

# Testes automatizados

docker-compose up tests

---

# Serviços

- db → PostgreSQL
- app → FastAPI
- tests → Pytest container

---

# Decisões arquiteturais

- Clean Architecture (camadas separadas)
- ETL isolado da infraestrutura
- Use Cases para regras de negócio
- Repository Pattern para banco
- Docker para consistência de ambiente
- Testes automatizados

---

Fluxo do sistema

1. Upload de CSV via API  
2. ETL (validação e transformação)  
3. Envio para API externa  
4. Persistência no PostgreSQL  
5. Geração de relatório  

---

Diferenciais

✔ Pipeline ETL estruturado  
✔ Arquitetura em camadas  
✔ Integração com API externa  
✔ Persistência em banco relacional  
✔ Testes automatizados  
✔ Docker Compose completo  
✔ Código limpo e modular  

---

Descrição para entrevista

Desenvolvi um pipeline de integração de dados com arquitetura em camadas, utilizando ETL para padronização de pedidos, integração com API externa e persistência em PostgreSQL. Todo o ambiente é containerizado com Docker e validado com testes automatizados.

---

Execução dos testes

docker-compose up tests

---

Resultado

✔ Sistema funcional  
✔ Arquitetura escalável  
✔ Testável  
✔ Containerizado  
✔ Pronto para produção simulada