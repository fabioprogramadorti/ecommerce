import csv
from app.domain.dtos.order_dto import OrderDTO

STATUS_MAP = {
    "PENDENTE": "PENDENTE",
    "APROVADO": "APROVADO",
    "CANCELADO": "CANCELADO",
    "ESTORNADO": "CANCELADO",
}

class CsvReader:

    def read(self, file_path: str, limit: int = None):
        orders = []

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for i, row in enumerate(reader):
                if limit and i >= limit:
                    break

                status_raw = (row.get("status") or row.get("status_pagamento")).strip().upper()
                status = STATUS_MAP.get(status_raw)

                if not status:
                    continue

                order = OrderDTO(
                    id_pedido=row["id_pedido"],
                    cliente=row["cliente"],
                    valor=row["valor"],
                    status=status
                )

                orders.append(order)

        return orders