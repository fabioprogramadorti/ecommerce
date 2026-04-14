import json
import pika
from sqlalchemy import create_engine, text


class OrderConsumer:

    def __init__(self):

        self.engine = create_engine(
            "postgresql://postgres:postgres@db:5432/orders"
        )

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='orders')

    def save(self, order):

        sql = """
        INSERT INTO orders (id_pedido, cliente, valor, status)
        VALUES (:id_pedido, :cliente, :valor, :status)
        """

        with self.engine.begin() as conn:
            conn.execute(text(sql), order)

    def callback(self, ch, method, properties, body):

        try:
            order = json.loads(body)

            print(f"[WORKER] Processando pedido {order['id_pedido']}")

            self.save(order)

            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            print(f"[ERROR] {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def run(self):

        self.channel.basic_consume(
            queue='orders',
            on_message_callback=self.callback
        )

        print("[WORKER] Rodando consumidor...")

        self.channel.start_consuming()