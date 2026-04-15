class ProcessOrdersUseCase:

    def __init__(self, repo=None, api=None, logger=None, producer=None):
        self.repo = repo
        self.api = api
        self.logger = logger
        self.producer = producer

    def execute(self, orders):

        if self.producer:
            self.logger.info(f"Enviando {len(orders)} pedidos para fila")
            self.producer.publish(orders)
            return

        success_orders = []
        failed_orders = []

        try:
            self.logger.info(f"Iniciando processamento de {len(orders)} pedidos")

            for order in orders:
                try:
                    self.api.send_order(order)
                    success_orders.append(order)
                except Exception:
                    failed_orders.append(order)

            if success_orders:
                self.repo.save_all(success_orders)

        finally:
            if self.repo:
                self.repo.close()