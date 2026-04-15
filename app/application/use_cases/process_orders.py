class ProcessOrdersUseCase:

    def __init__(self, producer, logger):
        self.producer = producer
        self.logger = logger

    def execute(self, orders):

        try:
            total = len(orders)

            if total == 0:
                self.logger.warning("Nenhum pedido recebido para processamento")
                return

            self.logger.info(f"Iniciando envio de {total} pedidos para fila")

            # envia todos os pedidos para a fila
            self.producer.publish(orders)

            self.logger.info(f"{total} pedidos enviados para RabbitMQ com sucesso")

        except Exception as e:
            self.logger.critical(f"Erro crítico ao enviar pedidos para fila: {str(e)}")