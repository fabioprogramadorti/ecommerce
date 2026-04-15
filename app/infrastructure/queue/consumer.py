import json
import time
import pika

from app.config.settings import settings
from app.infrastructure.api.rest_client import RestClient
from app.infrastructure.database.postgres_repository import PostgresRepository
from app.infrastructure.logging.logger import get_logger
from app.domain.dtos.order_dto import OrderDTO


class RabbitMQConsumer:

    def __init__(self):
        self.logger = get_logger()
        self.api = RestClient()
        self.repo = PostgresRepository()

        self.connection = self._connect_with_retry()
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='orders', durable=True)

    def _connect_with_retry(self):

        retries = 15

        for attempt in range(retries):
            try:
                self.logger.info(f"Tentando conectar ao RabbitMQ (tentativa {attempt+1})")

                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(
                        host=settings.RABBITMQ_HOST,
                        heartbeat=600,                     # 🔥 mantém conexão viva
                        blocked_connection_timeout=300     # 🔥 evita travamento
                    )
                )

                self.logger.info("Conectado ao RabbitMQ com sucesso")
                return connection

            except Exception as e:
                self.logger.warning(f"Falha ao conectar: {str(e)}")
                time.sleep(3)

        raise Exception("Não conseguiu conectar ao RabbitMQ")

    def callback(self, ch, method, properties, body):

        try:
            order_dict = json.loads(body)

            order = OrderDTO(
                id_pedido=int(order_dict["id_pedido"]),
                cliente=order_dict["cliente"],
                valor=float(order_dict["valor"]),
                status=order_dict["status"]
            )

            self.logger.info(f"Processando pedido {order.id_pedido}")

            self.api.send_order(order)

            self.repo.save(order)

            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            self.logger.error(f"Erro ao processar pedido: {str(e)}")

            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def start(self):

        self.channel.basic_qos(prefetch_count=1)

        self.channel.basic_consume(
            queue='orders',
            on_message_callback=self.callback
        )

        self.logger.info("Consumidor iniciado... aguardando mensagens")

        self.channel.start_consuming()


if __name__ == "__main__":
    RabbitMQConsumer().start()