class OrderDTO:
    def __init__(self, id_pedido, cliente, valor, status):
        self.id_pedido = int(id_pedido)
        self.cliente = cliente.strip()
        self.valor = float(valor)

        status = status.strip().upper()

        if status not in ["PENDENTE", "APROVADO", "CANCELADO","ESTORNADO", "RECUSADO"]:
            raise ValueError(f"Status inválido: {status}")

        self.status = status

    def __repr__(self):
        return f"OrderDTO(id={self.id_pedido}, cliente='{self.cliente}', valor={self.valor}, status='{self.status}')"