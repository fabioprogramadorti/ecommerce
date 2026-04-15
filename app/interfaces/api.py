from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os

from app.infrastructure.csv.csv_reader import CsvReader
from app.infrastructure.database.postgres_repository import PostgresRepository
from app.infrastructure.database.init_db import init_db
from app.infrastructure.logging.logger import get_logger
from app.infrastructure.queue.producer import RabbitMQProducer

from app.application.use_cases.process_orders import ProcessOrdersUseCase
from app.application.use_cases.generate_report import GenerateReportUseCase

app = FastAPI(
    title="Order Integration API",
    description="API para processamento de pedidos via CSV e integração com sistema externo",
    version="1.0.0"
)

init_db()


@app.get("/", summary="Health Check")
def root():
    return {"message": "API running"}


@app.post(
    "/orders/import",
    summary="Importar pedidos via CSV",
    description="Faz upload de um arquivo CSV e envia pedidos para processamento assíncrono",
)
async def import_orders(
    file: UploadFile = File(..., description="Arquivo CSV com pedidos")
):
    logger = get_logger()

    try:
        os.makedirs("data", exist_ok=True)

        filename = os.path.basename(file.filename)
        file_path = os.path.join("data", filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        reader = CsvReader()
        producer = RabbitMQProducer()

        orders = reader.read(file_path)

        ProcessOrdersUseCase(producer, logger).execute(orders)

        return {
            "message": "Pedidos enviados para processamento assíncrono",
            "processed": len(orders)
        }

    except Exception as e:
        logger.error(f"Erro ao importar pedidos: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar arquivo: {str(e)}"
        )


@app.get(
    "/orders/report",
    summary="Gerar relatório",
    description="Gera um relatório CSV com total de pedidos e valores por status"
)
def generate_report():

    logger = get_logger()

    try:
        os.makedirs("reports", exist_ok=True)

        repo = PostgresRepository()

        data = GenerateReportUseCase(repo).execute()

        return {
            "message": "Relatório gerado com sucesso",
            "file": "reports/report.csv",
            "data": data
        }

    except Exception as e:
        logger.error(f"Erro ao gerar relatório: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail=f"Erro ao gerar relatório: {str(e)}"
        )