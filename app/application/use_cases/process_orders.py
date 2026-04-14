class ProcessOrdersUseCase:

    def __init__(self, repo, api, logger):
        self.repo = repo
        self.api = api
        self.logger = logger

    def execute(self, orders):

        success_orders = []
        failed_orders = []

        try:
            self.logger.info(f"Iniciando processamento de {len(orders)} pedidos")

            for order in orders:
                try:
                    self.logger.info(f"Enviando pedido {order.id_pedido}")

                    self.api.send(order)

                    success_orders.append(order)

                except Exception as e:
                    failed_orders.append(order)

                    self.logger.error(
                        f"Erro ao enviar pedido {order.id_pedido}: {str(e)}"
                    )

            # salva SOMENTE os que deram certo na API
            if success_orders:
                self.repo.save_all(success_orders)
                self.logger.info(f"{len(success_orders)} pedidos salvos no banco")
            else:
                self.logger.warning("Nenhum pedido foi enviado com sucesso")

            # log de resumo final
            self.logger.info(
                f"Processamento finalizado | Sucesso: {len(success_orders)} | Falhas: {len(failed_orders)}"
            )

        except Exception as e:
            self.logger.critical(f"Erro crítico no processamento: {str(e)}")

        finally:
            self.repo.close()