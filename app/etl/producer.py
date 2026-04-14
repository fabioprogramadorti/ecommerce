import csv
import json
import pika


class OrderETLProducer:

    STATUS_MAP = {
        "pending": "PENDENTE",
        "approved": "APROVADO",
        "canceled": "CANCELADO"
    }

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq')  # Docker
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='orders')

    # EXTRACT
    def extract(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    # TRANSFORM
    def transform(self, orders):
        result = []

        for o in orders:
            result.append({
                "id_pedido": int(o["id_pedido"]),
                "cliente": o["cliente"],
                "valor": float(o["valor"]),
                "status": self.STATUS_MAP.get(
                    o["status"].lower(),
                    o["status"].upper()
                )
            })

        return result

    # LOAD (QUEUE)
    def publish(self, orders):

        for order in orders:
            self.channel.basic_publish(
                exchange='',
                routing_key='orders',
                body=json.dumps(order)
            )

    def run(self, file_path):

        raw = self.extract(file_path)
        clean = self.transform(raw)
        self.publish(clean)

        print(f"[ETL] {len(clean)} pedidos enviados para fila")