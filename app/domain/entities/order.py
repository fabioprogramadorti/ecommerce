class Order:
    def __init__(self, id_pedido, cliente, valor, status):
        self.id_pedido = int(id_pedido)
        self.cliente = cliente
        self.valor = float(valor)
        self.status = status.upper()
