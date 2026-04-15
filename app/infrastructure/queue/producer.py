import json
import time
import pika

from app.config.settings import settings
from app.infrastructure.logging.logger import get_logger


class RabbitMQProducer:

    def __init__(self):
        self.logger = get_logger()

        self.connection = self._connect_with_retry()
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='orders', durable=True)

    def _connect_with_retry(self):

        retries = 10

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

        raise Exception("Falha ao conectar no RabbitMQ")

    def publish(self, orders):

        for order in orders:
            try:
                self.channel.basic_publish(
                    exchange='',
                    routing_key='orders',
                    body=json.dumps(order.__dict__),
                    properties=pika.BasicProperties(
                        delivery_mode=2  # 🔥 mensagem persistente
                    )
                )

                self.logger.info(f"Pedido enviado para fila: {order.id_pedido}")

            except Exception as e:
                self.logger.error(
                    f"Erro ao enviar pedido {order.id_pedido}: {str(e)}"
                )